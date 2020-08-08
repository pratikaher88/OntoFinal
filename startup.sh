source newenv/bin/activate
docker-compose up -d
python manage.py migrate --database=hospital1
python manage.py migrate --database=hospital2
python manage.py migrate --database=mongo
python manage.py runserver