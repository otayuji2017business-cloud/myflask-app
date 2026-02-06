FROM python:3.12-slim

WORKDIR /app

# ★ pip を先にアップデート（ここが追加点）
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PORT=8080

CMD ["gunicorn", "-b", ":8080", "server:app"]
