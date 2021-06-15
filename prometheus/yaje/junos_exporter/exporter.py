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


from prometheus_client import make_wsgi_app
from wsgiref.simple_server import make_server
from junos_exporter.metrics import Metric
import yaml
import logging


class JunosExporter:
    def __init__(self, config_file: str=None, settings_file:str=None) -> None:
        logging.info('JunosExporter initialize')
        self.metrics = dict()
        self.device = dict()
        self.config_file = config_file or 'metrics.yml'
        self.settings_file = settings_file or 'settings.yml'
        with open(self.config_file, 'r') as f:
            try:
                config = yaml.safe_load(f)
                self.metrics = config.get('metrics')
            except yaml.YAMLError as e:
                logging.error(e)

        with open(self.settings_file, 'r') as f:
            try:
                config = yaml.safe_load(f)
                self.device = config.get('device')
            except yaml.YAMLError as e:
                logging.error(e)
        logging.debug('Metrics from config: {}'.format(self.metrics))
        logging.debug('Device param from config: {}'.format(self.device))
        # Create metric objects
        self.metric_list = [ Metric(metric=m) for m in self.metrics]

    def generate(self):
        logging.debug('Generate metrics')
        for metric in self.metric_list:
            metric.fetch(device=self.device)

metrics_app = make_wsgi_app()
je = JunosExporter()

def my_app(environ, start_fn):
    if environ['PATH_INFO'] == '/metrics':
        je.generate()
        return metrics_app(environ, start_fn)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M')
    print('Listening on port 3000')
    httpd = make_server('', 3000, my_app)
    httpd.serve_forever()
