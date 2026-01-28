from flask import Flask

app = Flask(__name__)
app.config.from_object('testapp.config') # 追加

from . import views
