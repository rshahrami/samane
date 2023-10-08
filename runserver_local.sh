#! /bin/bash

FILE=$PWD/.siteENV

if [ -f -a $FILE ]; then
    source .siteENV/bin/activate
    python config/manage.py runserver
else
    python3 -m venv .siteENV
    source .siteENV/bin/activate
    python config/manage.py runserver
fi
