FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /ontodesign

WORKDIR /ontodesign

ADD . /ontodesign/

RUN pip install -r requirements.txt

EXPOSE 8000

# ENTRYPOINT ["/entrypoint.sh"]