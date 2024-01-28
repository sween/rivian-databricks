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

ENV AWS_ACCESS_KEY_ID '123'
ENV AWS_SECRET_ACCESS_KEY '456'
ENV AWS_DEFAULT_REGION 'us-east-2'

CMD ["python" , "/src/rivian_deezwatts.py"]