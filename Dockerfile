FROM python:3.12-slim
WORKDIR /app
RUN pip install --no-cache-dir uv
COPY pyproject.toml README.md ./
COPY src ./src
RUN uv pip install --system .
EXPOSE 8000
CMD ["uvicorn", "ai_agent.api:app", "--host", "0.0.0.0", "--port", "8000"]
