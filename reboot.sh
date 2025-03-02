#!/user/bin/env bash

echo -e "------uwsgi deploy start------"

ps -ef | grep ./conf/uwsgi.ini | grep -v grep

sleep 0.5

echo -e "\n--- close ---"

ps -ef | grep ./conf/uwsgi.ini | grep -v grep | awk '{print $2}' | xarg kill -9

sleep 0.5

echo -e "\n--- check if the kill action is correct ---"

./venv/bin/uwsgi --ini ./conf/uwsgi.ini & > /dev/null

echo -e "------uwsgi started------"

sleep 1

ps -ef | grep ./conf/django_admin.ini | grep -v grep


