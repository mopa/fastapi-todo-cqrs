# Base Stage
FROM python:3.11-slim as base

ENV PIP_DEFAULT_TIMEOUT=100 \
    PYTHONUNBUFFERED=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app
COPY pyproject.toml ./

RUN python -c 'from urllib.request import urlopen; print(urlopen("https://install.python-poetry.org").read().decode())' | POETRY_HOME=/etc/poetry python3 - && \
    cd /usr/local/bin && ln -s /etc/poetry/bin/poetry && \
    poetry config virtualenvs.create false

ARG INSTALL_DEV=true
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main; fi"


# Final Stage
FROM base as final

COPY --from=base /app /app

RUN set -ex \
    # Create a user
    && addgroup --system --gid 1000 worker \
    && adduser --system --uid 1000 --gid 1000 --no-create-home worker \
    # Upgrades
    && apt-get update \
    && apt-get upgrade -y \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*


CMD ["uvicorn", "main:app", "--reload", "--workers", "1", "--host", "0.0.0.0", "--port", "8000"]

USER worker
