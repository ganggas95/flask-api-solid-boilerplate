import click
from flask import Flask


def init_cli(app: Flask):

    @click.command()
    def create_db():
        db = app.container.db.provided()
        db.create_database()

    app.cli.add_command(create_db)
