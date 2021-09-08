#!/bin/bash

echo "Installing packages for image: $1"

if [[ $1 = "latest" ]]
then
    cd /PostREISE
    pip install .
    cd /PowerSimData
    pip install .
elif [[ $1 = "stable" ]]
then
    pip install postreise
else
    echo "Unknown installation mode"
fi
