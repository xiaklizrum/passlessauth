FROM python:3.9.5
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --requirement requirements.txt