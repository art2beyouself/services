FROM python:3.7
LABEL maintainer "Montana"

ENV APP_HOME /app

WORKDIR $APP_HOME


COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    rm -rf requirements.txt

COPY . ./

EXPOSE 8000

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
