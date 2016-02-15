FROM tp33/django:1.2
ENV PYTHONUNBUFFERED 1
RUN mkdir /sockexchange
WORKDIR /sockexchange
ADD requirements.txt /sockexchange/
RUN pip install -r requirements.txt
ADD . /sockexchange/
CMD python SockExchange/manage.py runserver