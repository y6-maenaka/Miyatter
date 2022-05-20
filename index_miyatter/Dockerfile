From python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /index_miyatter_main
WORKDIR /index_miyatter_main
COPY requirements.txt /index_miyatter_main/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /index_miyatter_main/
