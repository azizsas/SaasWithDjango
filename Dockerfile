# Use Python 3.12 as base image
ARG PYTHON_VERSION=3.12-slim-bullseye
FROM python:${PYTHON_VERSION}

# Create virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip and configure Python
RUN pip install --upgrade pip
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev \
    libjpeg-dev \
    libcairo2 \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /code

# Copy requirements first for Docker cache optimization
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

# Copy entire project (including manage.py)
COPY . /code

# Cleanup to minimize image size
RUN apt-get remove --purge -y gcc \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Create startup script
ARG PROJ_NAME="project"
RUN echo "#!/bin/bash\n\
RUN_PORT=\${PORT:-8000}\n\
python manage.py migrate --no-input\n\
gunicorn ${PROJ_NAME}.wsgi:application --bind \"[::]:\$RUN_PORT\"" > paracord_runner.sh \
    && chmod +x paracord_runner.sh

# Start application
CMD ["./paracord_runner.sh"]