import argparse
import logging
from logging import handlers
import os

from flask import Flask

from .database import DB
from .database import create_tables

from .database.player import Player
from .database.tourny import Tourny

from .helpers.bphandler import BPHandler

def config_app(name):
    """
    Configure the Flask app before standing it up.

    :param name: string, Name of the flask app.
    :return: Flask object.
    """
    app = Flask(name)
    return app


def config_dabase(app):
    """
    Handle database configuration.

    Create the database directory, set the database path and add the database
    to the Flask app.
    :param app: configured Flask object.
    :return: None
    """
    app_path = '/opt/ironman'
    if not os.path.exists(app_path):
        os.mkdir(app_path)
    db_path = 'sqlite:///%s/ironman.db' % app_path
    app.config['SQLALCHEMY_DATABASE_URI'] = db_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    DB.app = app
    DB.init_app(app)


def setup_logging(debug=False, verbose=False):
    """
    Configure logging for the application.

    :param debug: Boolean, True will set log level to debug
    :param verbose: Boolean, True will set log level to info
    :return: None
    """
    logger = logging.getLogger()
    log_dir = '/opt/ironman'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    file_name = os.path.join(log_dir, 'ironman.log')
    logger.setLevel(logging.WARNING)
    if debug:
        logger.setLevel(logging.DEBUG)
    elif verbose:
        logger.setLevel(logging.INFO)
    fmt = '%(asctime)s - %(name)s %(levelname)s: %(message)s'
    formatter = logging.Formatter(fmt)

    term_channel = logging.StreamHandler()
    term_channel.setFormatter(formatter)
    logger.addHandler(term_channel)

    file_channel = handlers.RotatingFileHandler(file_name,
                                                maxBytes=4000000,
                                                backupCount=8)
    logger.addHandler(file_channel)



def launch():
    parser = argparse.ArgumentParser(description='Launch a API with routes '
                                                 'for a test application')
    parser.add_argument('-d', '--debug',
                        help='turn on the debug flag',
                        default=False,
                        action='store_true')
    parser.add_argument('-v', '--verbose',
                        help='turn on terminal output',
                        default=False,
                        action='store_true')
    subparser = parser.add_subparsers(dest='subcmd')
    subparser.required = True

    subparser.add_parser('init', help='setup the database')

    run = subparser.add_parser('run', help='run the app')

    run.add_argument('-p', '--port',
                     help='port to run the app on',
                     default=None)
    run.add_argument('-i', '--ip',
                     help='ip address to run the host at',
                     default=None)
    args = parser.parse_args()
    cmd = vars(args).pop('subcmd')
    setup_logging(args.debug, args.verbose)
    app = config_app('ironman')
    BPHandler.register_blueprints(app)
    config_dabase(app)

    if cmd == 'run':
        app.run(debug=args.debug, port=args.port)
    elif cmd == 'init':
        create_tables()
