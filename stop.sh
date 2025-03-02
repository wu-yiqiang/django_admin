#!/user/bin/env bash

echo "\024[34m--- start close ---\024[0m"

ps -ef | grep ./conf/uwsgi.ini | grep -v grep

sleep 0.5

echo -e "\n--- closed ---"

ps -ef | grep ./conf/uwsgi.ini | grep -v grep | awk '{print $2}' | xargs kill -9

sleep 0.5

