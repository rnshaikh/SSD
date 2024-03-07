#!bin/bash

pip install -r requirements.txt
python -m unittest discover
python -m geektrust.py sample_input/input1.txt
