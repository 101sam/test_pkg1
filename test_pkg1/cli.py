# -*- coding: utf-8 -*-

"""Console script for test_pkg1."""

import click


@click.command()
def main(args=None):
    """Console script for test_pkg1."""
    click.echo("Replace this message by putting your code into "
               "test_pkg1.cli.main")
    click.echo("See click documentation at http://click.pocoo.org/")


if __name__ == "__main__":
    main()
