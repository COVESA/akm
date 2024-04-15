# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10.13 AS base

# Install system dependencies required for Poetry
RUN apt-get update \
    && apt-get install -y curl git \
    # && apt-get install -y curl build-essential git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Poetry using recommended installer script
ENV POETRY_VERSION=1.7.0 \
    # Install Poetry globally
    POETRY_HOME="/usr/local" \
    POETRY_NO_INTERACTION=1 \
    # Ensure that the poetry path is in the PATH
    PATH="/usr/local/bin:$PATH"
    
# Install Poetry - respects $POETRY_VERSION
RUN curl -sSL https://install.python-poetry.org | python3 -

# Create a non-root user and switch to it
RUN useradd --create-home akm_user

# Switch to the non-root user
USER akm_user

CMD ["bash"]
