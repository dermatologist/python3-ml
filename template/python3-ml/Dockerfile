FROM python:3

RUN curl -sSL https://github.com/openfaas/faas/releases/download/0.13.0/fwatchdog > /usr/bin/fwatchdog \
    && chmod +x /usr/bin/fwatchdog
WORKDIR /root/

COPY index.py           .
COPY requirements.txt   .
RUN pip install -r requirements.txt

RUN mkdir -p function
RUN touch ./function/__init__.py
WORKDIR /root/function/
COPY function/requirements.txt	.
RUN pip install -r requirements.txt

WORKDIR /root/
COPY function           function
# Move the model/other assets
# RUN mv function/model.bin .


WORKDIR /root/

# Timeouts may be needed for ML workflows
# Tweak as needed.
ENV read_timeout=30
ENV write_timeout=30
ENV upstream_timeout=25
ENV fprocess="python3 index.py"

# Healthcheck interval increased from 1 to 10 s
HEALTHCHECK --interval=10s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
