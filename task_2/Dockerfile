# === Builder ===
FROM ubuntu:22.04 AS builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y ca-certificates python3 python3-venv && \
	rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY task_1/pyproject.toml task_1/uv.lock ./

RUN uv venv .venv && uv pip install --no-cache -r pyproject.toml

# === Runtime ===
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive PATH="/app/.venv/bin:$PATH"

RUN apt-get update && apt-get install -y python3 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv

COPY task_1/main.py .

CMD ["python", "main.py"]
