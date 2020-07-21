#!/usr/bin/env python3

import meinheld
import fire
def main(app):
    if app=="falcon":
        from falcon_app import application
    else:
        from flask_app import application


    meinheld.listen(("0.0.0.0", 8000))
    meinheld.run(application)
fire.Fire(main)