#!/bin/sh

set -e

cd ./nginx_proxy
docker build . -t mmantectrllayer/proxy:latest
