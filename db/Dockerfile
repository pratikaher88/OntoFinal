FROM postgres
COPY *.sql /docker-entrypoint-initdb.d/
ADD scripts/init.sql /docker-entrypoint-initdb.d
# RUN chmod a+r /docker-entrypoint-initdb.d/*
EXPOSE 5432