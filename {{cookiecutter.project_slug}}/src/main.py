"""
Contains the main typer application to run the Web API and to interface with the CLI
"""
from typing import Optional

import typer
import uvicorn

from utilities.settings import settings

app = typer.Typer()


@app.callback()
def main_settings(
        stage: Optional[str] = typer.Option(None)
):
    """
    Configure main settings for running commands via the CLI
    """
    if stage:
        settings.stage = stage


@app.command()
def start(reload: bool = typer.Option(True)):
    """
    Start the API with uvicorn
    """
    uvicorn.run('api:api', reload=reload)

# Add extra typers here


if __name__ == '__main__':
    app()
