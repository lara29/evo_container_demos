FROM python:3.9
LABEL type='yajep'
COPY requirements.txt /requirements.txt
COPY requirements_tf.txt /requirements_tf.txt
COPY entrypoint.sh /entrypoint.sh
COPY metrics.yml /metrics.yml
COPY settings.yml /settings.yml
COPY packages /project/packages

RUN python -m pip install -r requirements.txt
RUN pip install --no-index --find-links=file:///project/packages -r requirements_tf.txt

WORKDIR /

ENTRYPOINT [ "/entrypoint.sh" ]
# ENTRYPOINT ["tail", "-f", "/dev/null"]
