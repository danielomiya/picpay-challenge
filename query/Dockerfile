FROM debian:stable-slim

ARG Q_VERSION=2.0.19

RUN apt-get update && \
    apt-get install -y curl && \
    curl -sSLO https://github.com/harelba/q/releases/download/$Q_VERSION/q-text-as-data_$Q_VERSION-2_amd64.deb && \
    dpkg -i q-text-as-data_$Q_VERSION-2_amd64.deb && \
    rm q-text-as-data_$Q_VERSION-2_amd64.deb

ENTRYPOINT ["/bin/bash"]
CMD ["q", "-OHb", "-d", ",", "-q", "/usr/src/app/query.sql"]
