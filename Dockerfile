# ========== Base Image ==========
FROM python:3.11-slim

# ========== Set Working Directory ==========
WORKDIR /app

# ========== Copy Dependencies & Install ==========
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ========== Copy Entire Project ==========
COPY . .

# ========== Set Environment Path ==========
# (to make 'api/model_api.py' discoverable)
ENV PYTHONPATH=/app

# ========== Expose API Port ==========
EXPOSE 8000

# ========== Run the API ==========
CMD ["uvicorn", "api.model_api:app", "--host", "0.0.0.0", "--port", "8000"]
