FROM python:3-alpine

WORKDIR /usr/src/app

ENV PYTHONPATH "${PYTHONPATH}:${pwd}"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/main.py"]
