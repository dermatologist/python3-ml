ARG watchdog_version=0.2.2
ARG conda_version=4.12.0
FROM --platform=${TARGETPLATFORM:-linux/amd64} ghcr.io/openfaas/classic-watchdog:${watchdog_version} as watchdog
FROM --platform=${TARGETPLATFORM:-linux/amd64} continuumio/miniconda3:${conda_version} as build


COPY --from=watchdog /fwatchdog /usr/bin/fwatchdog
RUN chmod +x /usr/bin/fwatchdog

ARG ADDITIONAL_PACKAGE
# Alternatively use ADD https:// (which will not be cached by Docker builder)
ARG CHANNEL=pytorch

RUN apt-get -qy update \
  && apt-get -qy install gcc make ${ADDITIONAL_PACKAGE} \
  && rm -rf /var/lib/apt/lists/*

# Add non root user
RUN addgroup --system app && adduser app --system --ingroup app
RUN chown app /home/app

USER app

ENV PATH=$PATH:/home/app/.local/bin

WORKDIR /home/app/

COPY --chown=app:app index.py           .
COPY --chown=app:app requirements.txt   .

USER root
RUN while read requirement; do conda install --yes $requirement -c ${CHANNEL} || pip install $requirement; done < requirements.txt

# Build the function directory and install any user-specified components
USER app



FROM build as ship
WORKDIR /home/app/

#configure WSGI server and healthcheck
USER app

ENV fprocess="python index.py"

ENV cgi_headers="true"
ENV mode="http"
ENV upstream_url="http://127.0.0.1:5000"
ENV exec_timeout="1m30s"
ENV write_timeout="1m30s"
ENV read_timeout="1m30s"
ENV RAW_BODY="false"

HEALTHCHECK --interval=5s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]