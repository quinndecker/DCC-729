web: gunicorn DCC_Site_2.wsgi
--log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate