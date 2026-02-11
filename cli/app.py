import typer
from core.dispatcher import Dispatcher

app = typer.Typer()


@app.command()
def translate(
    text: str,
    source: str = "en",
    target: str = "pt",
    provider: str = typer.Option(None, "--provider", "-p"),
):
    dispatcher = Dispatcher(provider=provider)
    result = dispatcher.translate(text, source, target)
    typer.echo(result)


@app.command()
def transliterate(
    text: str,
    language: str,
    script: str,
    provider: str = typer.Option(None, "--provider", "-p"),
):
    dispatcher = Dispatcher(provider=provider)
    result = dispatcher.transliterate(text, language, script)
    typer.echo(result)


if __name__ == "__main__":
    app()
