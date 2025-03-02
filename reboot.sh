#!/user/bin/env bash

echo -e "\033[34m---uwsgi deploy start---\033[0m"

ps -ef | grep ./conf/uwsgi.ini | grep -v grep

sleep 0.5

echo -e "\n--- close ---"

ps -ef | grep./conf/uwsgi.ini | grep -v grep | awk '{print $2}' | xarg kill -9

sleep 0.5

echo -e "\n--- check if the kill action is correct---"

/enus/django_admin/bin/uwsgi --ini ./conf/uwsgi.ini & >/dev/null

echo -e "\033[34m---uwsgi started---\033[0m"

sleep 1

ps -ef | grep ./conf/django_admin.ini | grep -v grep


