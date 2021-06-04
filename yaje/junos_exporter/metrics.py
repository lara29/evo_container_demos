# Copyright 2021 lrajan@juniper.net
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import logging
from prometheus_client import Gauge, Enum, Info
from jnpr.junos import Device


class Metric:
    def __init__(self, metric: dict=None, device:dict=None) -> None:
        self.metric = metric
        self.gauges = dict()

    def fetch(self, device) -> dict:
        logging.debug('Fetching for :'.format(device['ip']))
        with Device(host=device['ip'], user=device['user'], passwd=device['password'],
                    port=device['port'], auto_probe=5) as dev:

            data_xml = dev.rpc.get_interface_information({'format': 'xml'}, terse=True, normalize=True)
            for item in data_xml.xpath(self.metric.get('rpc-response')['list_key']):
                for field in self.metric.get('rpc-response')['fields']:
                    unique_id = item.findtext(field.get('unique_id','')).replace('/','_').replace(':', '_')
                    metric_name = '{}_{}'.format(unique_id, field['name'],).replace('-','_')
                    logging.debug('metric_name: ', metric_name)
                    metric = self.gauges.get(metric_name)
                    if metric is None:
                        logging.debug(f'Metric {metric_name} not available!, creating')
                        metric = Info(metric_name, metric_name)
                        self.gauges[metric_name] = metric
                    values =  dict()
                    for key in field['keys']:
                        logging.debug('key:', key)
                        values[key.replace('-','_')] = item.findtext(key)
                    logging.debug('values: ', values)
                    metric.info(values)

        return self.gauges
