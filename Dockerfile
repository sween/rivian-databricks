FROM python:3.8

ADD src /src

RUN pip install plotly
RUN pip install polyline
RUN pip install python-dateutil
RUN pip install python-dotenv
RUN pip install requests
RUN pip install geopy
RUN pip install boto3

WORKDIR /src


ENV PYTHONPATH '/src/'
ENV RIVIAN_PASSWORD 'secret'
ENV RIVIAN_USERNAME 'k8s'

ENV AWS_ACCESS_KEY_ID ''
ENV AWS_SECRET_ACCESS_KEY= ''
ENV AWS_DEFAULT_REGION= ''

CMD ["python" , "/src/rivian_deezwatts.py"]