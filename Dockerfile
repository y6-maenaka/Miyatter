From python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /outon_main
WORKDIR /outon_main
COPY requirements.txt /outon_main/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /outon_main/
