FROM beapen/fastai-vision

# Allows you to add additional packages via build-arg
ARG ADDITIONAL_PACKAGE
ARG CHANNEL=pytorch

RUN addgroup app && adduser app --system --ingroup app \
    && chown -R app /root && chmod -R go+rX /root

ENV HOME /home/app

RUN apt-get update \
    && apt-get -y install curl bzip2 ${ADDITIONAL_PACKAGE} \
    && curl -sSL https://github.com/openfaas-incubator/of-watchdog/releases/download/0.5.1/of-watchdog > /usr/bin/fwatchdog \
    && apt-get -qq -y remove curl \
    && apt-get -qq -y autoremove \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /var/log/dpkg.log \
    && chmod +x /usr/bin/fwatchdog

# Add non root user
WORKDIR /home/app/
USER app


COPY requirements.txt   .
RUN conda install -n fastai-vision --file requirements.txt -c ${CHANNEL}
COPY index.py           .

RUN mkdir -p function
RUN touch ./function/__init__.py

WORKDIR /home/app/function/
COPY function/requirements.txt    .
RUN conda install -n fastai-vision --file requirements.txt -c ${CHANNEL}

WORKDIR /home/app/
COPY function/ ./function

# Timeouts may be needed for ML workflows
# Tweak as needed.
ENV read_timeout=30
ENV write_timeout=30
ENV upstream_timeout=25
ENV fprocess="/opt/conda/envs/fastai-vision/bin/python3 index.py"
ENV function_root="/home/app/function"
RUN conda init bash
RUN echo "conda activate fastai-vision" >> /home/app/.bashrc

# Healthcheck interval increased from 1 to 10 s
HEALTHCHECK --interval=10s CMD [ -e /tmp/.lock ] || exit 1

CMD ["fwatchdog"]
