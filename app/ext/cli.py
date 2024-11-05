import click

from ext.database.commands import create_database, drop_database

def init_app(app):

    app.cli.add_command(app.cli.command()(create_database))
    app.cli.add_command(app.cli.command()(drop_database))