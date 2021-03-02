#!/bin/bash
#
# Responsible for running one-time task(s) required to setup the application locally.
#
# NOTE: This script expects to be run from the project root with
# ./scripts/bootstrap.sh

set -o pipefail

if [ ! -f 'environment.sh' ]; then
echo "
export NOTIFY_ENVIRONMENT='development'

export MMG_API_KEY='MMG_API_KEY'
export FIRETEXT_API_KEY='FIRETEXT_ACTUAL_KEY'
export NOTIFICATION_QUEUE_PREFIX='YOUR_OWN_PREFIX'

export FLASK_APP=application.py
export FLASK_ENV=development
export WERKZEUG_DEBUG_PIN=off

export SQLALCHEMY_DATABASE_URI='postgresql://db:password@localhost:5432/notification_api'
"> environment.sh
fi

./update_dependencies_and_migrate_db.sh
