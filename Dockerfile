FROM mcr.microsoft.com/playwright/python:v1.49.0-jammy

WORKDIR /app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY pytest.ini ./
COPY UI ./UI

# Run the UI suite by default; reports/screenshots land under /app.
CMD ["python", "-m", "pytest", "UI/POM/Tests"]
