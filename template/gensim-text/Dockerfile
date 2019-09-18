FROM openfaas/classic-watchdog:0.15.4 as watchdog

FROM beapen/gensim-text

# Allows you to add additional packages via build-arg
ARG ADDITIONAL_PACKAGE
ARG CHANNEL=anaconda

COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

# Uncomment if additional packages are required.
# RUN apt-get update \
#    && apt-get -y install ca-certificates ${ADDITIONAL_PACKAGE}



# Add non root user
RUN addgroup app && adduser app --system --ingroup app

WORKDIR /home/app/

COPY index.py           .
COPY requirements.txt   .

RUN chown -R app /home/app && \
  mkdir -p /home/app/python && chown -R app /home/app
USER app
ENV PATH=$PATH:/home/app/.local/bin:/home/app/python/bin/
ENV PYTHONPATH=$PYTHONPATH:/home/app/python

# No dependencies defined in the template
# RUN pip install -r requirements.txt --target=/home/app/python

RUN mkdir -p function
RUN touch ./function/__init__.py

WORKDIR /home/app/function/
COPY function/requirements.txt	.

# Uncomment if your function has dependencies
# RUN pip install -r requirements.txt --target=/home/app/python

WORKDIR /home/app/

USER root

COPY function           function

RUN chown -R app:app ./ && \
  chmod -R 777 /home/app/python

USER app

# Timeouts may be needed for ML workflows
# Tweak as needed.
ENV read_timeout=30
ENV write_timeout=30
ENV upstream_timeout=25
ENV fprocess="python3 index.py"
ENV function_root="/home/app/function"
EXPOSE 8080

# Healthcheck interval increased from 3 to 10 s
HEALTHCHECK --interval=10s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
