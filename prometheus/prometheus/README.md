### Prometheus
Use the prom/prometheus for running Prometheus, or binary could be used.

The prometheus config file contains details about the different exporters from which
 Prometheus will poll the data at given intervals. Volume mount this file onto the
  Prometheus container as follows:
```
docker run -d --restart unless-stopped --network=host --name=prometheus
           -v /home/root/prometheus.yml:/etc/prometheus/prometheus.yml prom/prometheus
```
