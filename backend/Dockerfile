FROM python:3.11.8-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt
COPY app.py .
COPY services.py .
COPY controller.py .
COPY questions.db .
COPY users.db .
COPY career_recommendation_system.pkl .
COPY db/ db/
EXPOSE 5000
CMD ["python3", "app.py"]