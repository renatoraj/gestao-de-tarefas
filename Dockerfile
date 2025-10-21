FROM python:3.9-slim
ENV PYTHONPATH=/app
WORKDIR /app
RUN echo "Flask" > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]