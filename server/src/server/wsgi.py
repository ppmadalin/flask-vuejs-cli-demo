# coding: utf-8

from server.flask_app import create_app

app = create_app(env="PROD")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
