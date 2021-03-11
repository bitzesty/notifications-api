#!/usr/bin/env python
import sentry_sdk

from flask import Flask

# notify_celery is referenced from manifest_delivery_base.yml, and cannot be removed
from app import notify_celery, create_app  # noqa
from sentry_sdk.integrations.celery import CeleryIntegration

sentry_sdk.init(
    integrations=[CeleryIntegration()],
    traces_sample_rate=1.0
)


application = Flask('celery')
create_app(application)
application.app_context().push()
