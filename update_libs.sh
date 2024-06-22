#!/bin/bash

# TODO: make sure script is executable first
#chmod +x update_libs.sh

# to run script
#./update_libs.sh

# Update all libraries listed in requirements.txt
pip install --upgrade -r requirements.txt

# Verify installed versions
pip list

# Generate updated requirements.txt
pip freeze > requirements.txt

echo "Libraries updated and requirements.txt refreshed."
