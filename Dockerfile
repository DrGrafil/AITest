FROM ubuntu:17.04

RUN apt-get update
RUN apt-get install -y openssh-server vim man

# Here is a good spot to add setup script like `pip install package`
# to ensure is not constantly rebuilt.

ENV HOME=/root
WORKDIR /root/
COPY docker.py docker.py
RUN python3 -c "from docker import setup_ssh; setup_ssh()"
COPY . /root/
