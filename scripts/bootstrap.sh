#!/bin/bash
#
# Bootstrap virtualenv environment and postgres databases locally.
#
# NOTE: This script expects to be run from the project root with
# ./scripts/bootstrap.sh

set -o pipefail

if [ ! $VIRTUAL_ENV ]; then
  virtualenv -p python3 ./venv
  . ./venv/bin/activate
fi

# we need the version file to exist otherwise the app will blow up
make generate-version-file

# Install Python development dependencies
pip3 install -r requirements_for_test.txt

# Upgrade databases
source environment.sh
flask db upgrade
