FROM ubuntu

ENV Q_VERSION 2.0.19

RUN apt update && \
    apt install -y curl && \
    curl -sSLO https://github.com/harelba/q/releases/download/$Q_VERSION/q-text-as-data_$Q_VERSION-2_amd64.deb && \
    dpkg -i q-text-as-data_$Q_VERSION-2_amd64.deb && \
    rm q-text-as-data_$Q_VERSION-2_amd64.deb

ENTRYPOINT ["/bin/bash"]
CMD ["q", "-OHb", "-d", ",", "-q", "/usr/src/app/query.sql"]
