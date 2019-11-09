#!/usr/bin/env python
# -*- coding: utf-8 -*-
# flask appの初期化を行い、flask appオブジェクトの実体を持つ
from flask import Flask
from flasks.database import init_db
import flasks.models


def create_app():
    app = Flask(__name__)
    app.config.from_object('flasks.config.Config')
    init_db(app)

    return app


app = create_app()
