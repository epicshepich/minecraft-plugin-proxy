#!/bin/sh

. ./.env

echo $GHCR_TOKEN | podman login ghcr.io -u USERNAME --password-stdin

podman push ghcr.io/epicshepich/minecraft-plugin-proxy:latest
podman push ghcr.io/epicshepich/minecraft-plugin-proxy:$(cat ./.version)