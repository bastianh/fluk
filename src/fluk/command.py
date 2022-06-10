import os

import click
from click import ParamType
from click.shell_completion import CompletionItem


class EnvVarType(ParamType):
    name = "envvar"

    def shell_complete(self, ctx, param, incomplete):
        return [
            CompletionItem(name) for name in os.environ if name.startswith(incomplete)
        ]


@click.command()
@click.option("--ev", type=EnvVarType(), help="environemt name")
def cli(ev):
    click.echo(f"Name: {ev}")
    click.echo(f"Value 2: {os.environ.get(ev)}")
