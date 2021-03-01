##!/usr/bin/env python
from __future__ import print_function

import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

from app import create_app

sentry_sdk.init(
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

application = Flask('app')

create_app(application)
