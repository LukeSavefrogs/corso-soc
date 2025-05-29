# FROM php:8.2-apache
# RUN docker-php-ext-install mysqli pdo pdo_mysql
# RUN docker-php-ext-enable mysqli
FROM ubuntu:22.04
RUN apt-get clean && apt-get -y update && apt-get -y upgrade && apt-get -y install libffi-dev git python3 python3-venv python3-pip
RUN <<-EOF
    mkdir xss-demo && cd xss-demo
    git clone https://github.com/omarkohl/xss-demo.git
    python3 -m venv .venv
    . .venv/bin/activate
    python3 -m pip install -U setuptools && python3 -m pip install -U pip
    cd xss-demo/app
    python3 -m pip install -r dev_requirements.txt
    python3 setup.py develop
EOF

CMD [ "pserve", "development.ini" ]