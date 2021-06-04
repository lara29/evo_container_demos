### Snmp exporter
This folder contains files necessary for running the snmp exporter container on Evo.

`generator.yml` contains the config necessary to generate the `snmp.yml` file that
 needs to be volume mounted while running the snmp exporter container. Please
  follow the instructions at https://github.com/prometheus/snmp_exporter/tree/main
  /generator to generate snmp.yml. Ensure that the right IP address and
   credentials are provided to the generator.yml.
  
The image used to run the snmp-exporter is `prom/snmp-exporter`.

The container can be run on Evo as follows:
```
docker run -d --restart unless-stopped --network=host --name=snmp_exporter
           -v /home/root/snmp.yml:/etc/snmp_exporter/snmp.yml prom/snmp-exporter
```