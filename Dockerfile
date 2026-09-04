FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml README.md ./
COPY factory ./factory
COPY products ./products
RUN pip install --no-cache-dir -e .
CMD ["python", "-m", "factory"]
