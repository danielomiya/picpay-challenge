#!/bin/bash

# wait until data ingest is done
sleep 3

q -OHb -d , -q /usr/src/app/query.sql
