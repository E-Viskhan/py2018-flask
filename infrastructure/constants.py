from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = False


# TODO: Путь к бд может быть другим!
DATABASE = 'database.sqlite'
