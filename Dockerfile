FROM mcr.microsoft.com/playwright/python:v1.30.0-focal

WORKDIR /app

COPY /UI/POM/Pages /app/Pages 
COPY /UI/POM/Tests /app/Tests
COPY /UI/POM/utils /app/utils

RUN python -m pip install --upgrade pip
RUN pip install playwright pytest
RUN playwright install