source newenv/bin/activate
pip install -r requirements.txt
docker-compose up -d
python3 manage.py migrate --database=hospital1
python3 manage.py migrate --database=hospital2
python3 manage.py migrate --database=mongo
python3 manage.py runserver