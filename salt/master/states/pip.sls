python-pip:
  pkg.installed:
    - pkgs:
      - python-pip
      - python3-pip

junos-eznc:
  pip.installed:
    - name: junos-eznc
    - bin_env: '/usr/bin/pip3'
    - require:
      - pkg: python-pip
