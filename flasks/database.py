#!/usr/bin/env python
# -*- coding: utf-8 -*-
# FlaskアプリがSQLAlchemyを使えるようにするための初期化
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)
    Migrate(app, db)
