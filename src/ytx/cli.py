import typer

app = typer.Typer()

@app.command()
def hello():
    print("Hello world from ytx!")

@app.command()
def version():
    print("ytx 0.1.0")

if __name__ == "__main__":
    app()