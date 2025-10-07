#!/bin/bash
export PATH=$PATH:/vercel/.local/bin
python3.9 -m pip install --upgrade pip
python3.9 -m pip install -r requirements.txt
python3.9 manage.py collectstatic --no-input --clear
