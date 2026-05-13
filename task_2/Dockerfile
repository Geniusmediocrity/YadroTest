# === Builder ===
FROM ubuntu:22.04 AS builder

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y ca-certificates python3 python3-venv python3-pip && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY task_1/pyproject.toml ./

RUN python3 -m venv .venv && .venv/bin/pip install .

# === Main app ===
FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive PATH="/app/.venv/bin:$PATH"

RUN apt-get update && apt-get install -y python3 && \
    rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv

COPY task_1/main.py .

CMD ["python", "main.py"]
