#!/bin/bash
pyinstaller --onefile --add-data "images:images" --add-data "icons:icons" --add-data "sound:sound" main.py