#!/bin/bash
ln -snv /PostRIESE/postreise/plot/demo /plug/nbcopy
jupyter lab --port=10000 --no-browser --ip=0.0.0.0 --allow-root
