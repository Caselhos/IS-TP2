#!/bin/bash

npm install;

npx prisma generate;
#npx prisma db pull
if [ "$USE_DEV_MODE" = "true" ];
  then npm run start:dev;
  else npm run start;
fi