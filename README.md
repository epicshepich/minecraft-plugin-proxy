# Minecraft Plugin Proxy

Are you a Minecraft sysadmin using a containerized setup? Are you sick of dealing with plugins that don't support downloading the latest version via REST API? Then this is the project for you!

This project is a proxy server that will find the latest version of a plugin and redirect you to the download link. 

All of the plugins have custom hard-coded logic that will find the latest version of the plugin and redirect you to the download link.

## Usage

Include the minecraft-plugin-proxy as a service in your compose unit:

```yaml
services:
  minecraft-plugin-proxy:
    image: ghcr.io/epicshepich/minecraft-plugin-proxy:latest
```

Services in your compose unit can access the proxy server at `http://minecraft-plugin-proxy:8080` with the following query parameters:


## Endpoints

The following endpoints are currently available:

- `/viabackwards/velocity`: ViaBackwards for the Velocity proxy container.
- `/luckperms/{server_type}`: LuckPerms for the specified server type (e.g. `bukkit`, `bungeecord`, `velocity`).
- `/tribufu-velocityrcon`: Tribufu's VelocityRcon plugin for the Velocity proxy container.