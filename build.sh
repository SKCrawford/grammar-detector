#!/bin/bash

rm -r ./dist/
rm -r ./**.egg-info/
python -m build
