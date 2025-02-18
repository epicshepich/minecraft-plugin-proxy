#!/bin/sh

podman build \
    -t ghcr.io/epicshepich/minecraft-plugin-proxy:latest \
    -t ghcr.io/epicshepich/minecraft-plugin-proxy:$(cat ./.version) \
    .