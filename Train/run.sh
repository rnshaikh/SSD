#!/bin/bash

pip install requirements.txt
python -m unittest discover
python -m geektrust.py -m sample_input/input1.txt
