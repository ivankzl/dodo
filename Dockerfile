ENV PYTHONUNBUFFERED 1

#RUN mkdir /code
WORKDIR /code

ENV PYTHONPATH=/code
ADD ./requirements/base.txt /tmp
ADD ./requirements/development.txt /tmp

RUN pip install -r /tmp/base.txt
RUN pip install gunicorn
RUN pip install -r /tmp/development.txt

ADD . /code/
