#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS="/Users/hyunc/Desktop/HackNC/Recyclable_Products-d27862b02892.json"
export IMAGE_PATH='/Users/hyunc/Desktop/HackNC/plastic_bag_test.jpg'
export PROJECT_ID='394744105300'
export MODEL_ID='ICN5787798422287286272'

python3 recycle.py
