# coding: utf-8

from server.flask_app import create_app
from server.manage import init_db

app = create_app(env="DEV")

app.cli.add_command(init_db)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
