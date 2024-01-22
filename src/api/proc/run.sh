#!/bin/bash

if [ "$USE_DEV_MODE" = "true" ];
  then nodemon --exec python -u djangotest/manage.py runserver 0.0.0.0:8080;#$API_PORT;
  else python -u djangotest/manage.py runserver 0.0.0.0:8080;
fi