#!/user/bin/env bash

echo "------ start close ------"

ps -ef | grep ./conf/uwsgi.ini | grep -v grep

sleep 0.5

echo "\n--- closed ---"

ps -ef | grep ./conf/uwsgi.ini | grep -v grep | awk '{print $2}' | xargs kill -9

sleep 0.5

