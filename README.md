### Running container on Evo Devices
Juniper devices running the Evo OS are capable of running Docker containers and
 this opens up a lot of opportunities for running custom third party apps that can
  interact with the Evo device.

  This repository contains the below two use-cases:

 a) Salt Master and Minion, where the minion runs on the Evo device and is used by
  the master to get device facts and push a sample config into the device.

 b) Prometheus monitoring using two exporters - a) snmp exporter,
  and b) custom junos exporter, both of which runs on Evo and is used to collect
   metrics by a Prometheus instance running on en external host.

 The repo contains the necessary files and configs to demonstrate the above two
  use-cases.
