#!/bin/sh

podman build -t minecraft-plugin-proxy:latest -t minecraft-plugin-proxy:$(cat ./.version) .