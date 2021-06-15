FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y salt-minion && \
    apt-get install -y net-tools && \
    apt-get install -y iputils-ping && \
    apt-get install -y telnet && \
    apt install -y python3-pip && \
    python3 -m pip install --upgrade pip && \
    pip3 install --ignore-installed PyYAML && \
    pip3 install junos-eznc && \
    pip3 install jxmlease yamlordereddictloader

COPY entrypoint.sh /

CMD ["sh", "/entrypoint.sh"]
