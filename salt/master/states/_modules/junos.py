import logging
import json
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from pprint import pprint

log = logging.getLogger(__name__)

__virtual_name__ = 'junos'


def facts():
    print('Calling facts in minion')
    dev = Device(port=22, host='10.49.166.19', user='root', password='xxxx')
    dev.open()
    pprint(dev.facts)
    facts = json.dumps(dev.facts)
    dev.close()
    return facts

def config_example():
    success = 'True'
    with Device(host='10.49.166.19', user='root', password='xxxx', port=22) as dev:
        cu = Config(dev)
        data = "set interfaces et-1/0/1 unit 0 family inet"
        cu.load(data, format='set')
        cu.pdiff()
        if cu.commit_check():
            cu.commit()
        else:
            cu.rollback()
            success = 'False, unable to commit'

    return success
