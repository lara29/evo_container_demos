# YAJE
### Yet Another Junos Exporter

I had difficulty getting to run the existing third party Junos exporters on Evo
, and so ended up writing this very simple version. Use it only for demo and any
contributions are welcome.

Pass in the device credentials in `settings.yml`. Note that as of now, this file
is not volume mounted but added as part of the image. By default, YAJE listens on
port `3000`. The image needs to be built and moved to the Evo device.


YAJE can be run using the below command:
```
docker run -d --restart unless-stopped --network=host --name=junos_exporter
              --cap-add=NET_ADMIN --env-file=/run/docker/jnet.env lara/junos_exporter
```
