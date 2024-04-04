FROM python

WORKDIR /app

COPY main.py ./
RUN pip install fastapi
RUN pip install "uvicorn[standard]"

CMD [ "uvicorn","main:app","--reload","--host","0.0.0.0"]