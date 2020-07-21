#!/usr/bin/env python3

import bjoern
import fire

def main(app):
    if app=="falcon":
        from falcon_app import application
    else:
        from flask_app import application

    bjoern.run(
        wsgi_app=application,
        host='0.0.0.0',
        port=8000,
        reuse_port=True
    )

fire.Fire(main)