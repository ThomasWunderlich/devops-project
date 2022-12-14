# Build the Python container
FROM python:3.10-slim-bullseye AS base
# Ideally this should be from scratch, but that would require bundling the app as a pex binary, which would take a bit
# more time than I'd like for this test
SHELL ["/bin/bash", "-c"]
RUN adduser \
        --disabled-password \
        --gecos '' \
        --home /home/stellar \
        --shell /bin/bash \
        stellar

USER stellar

WORKDIR /home/stellar
ENTRYPOINT ["/bin/bash", "-o", "errexit", "-o", "nounset", "-c"]

FROM base AS fib-app
COPY --chown=stellar:stellar . .

# TODO set up a prod WSGI server like gunicorn
ENTRYPOINT ["python", "fib/main.py"]

