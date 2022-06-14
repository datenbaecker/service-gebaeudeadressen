FROM python:3.9

#RUN apt-get --assume-yes install python3-pip
RUN groupadd -r addressprovider && useradd --no-log-init -r -g addressprovider addressprovider

COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

ADD app /app

RUN chown -R addressprovider:addressprovider /app

USER addressprovider

WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
