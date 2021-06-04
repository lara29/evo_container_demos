### Running Salt Minion
The salt minion container is run on the Evo device, and this communicates with the
 Salt master container.
 
Create the minion docker image using the command
```
docker build -t lara/minion .
```
This image needs to be built on a different host which supports docker build and
 moved into the Evo device. The time this readme is written, docker build was not
  supported on the Evo device.

The salt minion can be run on the Evo device using the command:
```
docker run -d --restart unless-stopped --network=host 
              --name=minion --hostname=minion
              --volume=/data:/data:ro --volume=jnet:/usr/evo
              --cap-add=sys_admin --cap-add=net_admin
              --env-file=/run/docker/jnet.env
              -v /home/root/minion/minion.conf:/etc/salt/minion lara/minion
```
From the above command, we can see that we need to volume mount the minion.conf
 file to /etc/salt/minion. This file should contain the IP of the host running
  salt master container.
  
We are hooking the container onto the host network instead of a bridge. Also
 notice the additional parameters passed in to support Docker networking in Evo.
 
The minion id is defined in the `entrypoint.sh` and is `vscapa_minion` by default.
 
 
###Running Salt Master
The Salt Master container is run external to the Evo device. There are a couple of
 files that need to be volume mounted to the Master container.
 
 a) master.conf: This file defines the base directory for srv and pillar root.
 
 b) /states : This folder contains the pillars that defines the packages that need
  to be installed in the minion (top.sls and pip.sls). For now, we don't need to
   install packages
   using
   salt as the minion container already contains the necessary packages installed
   . This is just to serve as an example for reference.
   
 c) /states/_modules : This contains the user defined modules that can bee synced
  with the minion and executed on the target device from the master or minion.
  
 The command for running the salt master is:
 ```
docker run -d --network=host --name master --hostname salt 
                  -v /root/master/master.conf:/etc/salt/master 
                  -v /root/master/states:/srv/salt 
                  -v /root/master/proxy.conf:/etc/salt/proxy lara/master
```

### Testing the master-minion communication
a. Login to the master container and execute `salt-key -L` to list the keys. The
 minion id
 should
 be present in the `Unaccepted Keys` list

b. Accept the keys using the command `salt-key -A`. Upon listing the keys again
, the minion id should be visible in the `Accepted Keys` list.

c. Test master-minion communication by running the command `salt '*' test.ping
`. This should return `True`.

### Running custom modules
The custom modules should be placed in the folder `_modules`. In our case, we have
 the junos.py module which contains two functions `facts` and `config_example`.
 
First, we sync the module with minion in case any changes were made to junos.py.
```
salt '*' saltutil.sync_modules
```

Once the module is synced, we can execute the function from the master like below:
```
salt '*' junos.facts
```
This executes the function facts() which is a simple fn that returns the device
 facts.
 
Similarly, config example executes a config push of a hardcoded set command.
More complicated usecases can be build from these. Also, take a look at integrating 
 the junos proxy minion that has functions to perform generic operations on Evo.