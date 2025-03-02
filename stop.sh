#!/user/bin/env bash

echo -e "\033[34m---uwsgi deploy start---\033[0m"

ps -ef | grep ./conf/uwsgi.ini | grep -v grep

sleep 0.5

echo -e "\n--- close ---"

ps -ef | grep./conf/uwsgi.ini | grep -v grep | awk '{print $2}' | xargs kill -9

sleep 0.5

