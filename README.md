# Keida Hub for Unraid

This repository provides the Unraid Docker template for Keida Hub.

Keida Hub is distributed as a public Docker image through GitHub Container Registry. No GitHub account, source-code checkout, Python installation, Node installation, or local build is required.

## Install on Unraid

### 1. Download the Keida Hub template

Open an Unraid terminal and run:

    curl -fsSL 'https://raw.githubusercontent.com/Hizumi-Senpai/Keida-Hub-Unraid/main/templates/keida-hub.xml' -o /boot/config/plugins/dockerMan/templates-user/my-keida-hub.xml

    chmod 600 /boot/config/plugins/dockerMan/templates-user/my-keida-hub.xml

### 2. Open the template

In the Unraid WebUI:

1. Open Docker.
2. Click Add Container.
3. Open the Template dropdown.
4. Select keida-hub.

If it does not appear immediately, refresh the Add Container page once.

### 3. Review the defaults

The template uses:

- Docker image: ghcr.io/hizumi-senpai/keida-hub:beta
- Network: bridge
- WebUI port: 8787
- Appdata: /mnt/user/appdata/keida-hub
- Container config path: /config
- Privileged mode: disabled

If port 8787 is already in use, change only the host-side WebUI port.

### 4. Install

Click Apply and allow Unraid to download and start the container.

When installation finishes, open the Keida Hub WebUI and complete the first-run setup.

## Updates

Beta installations follow the :beta container tag.

When a new Keida Hub beta is published, Unraid can detect the updated Docker image through its normal container update system.

Persistent configuration and the Keida Hub database are stored outside the container in /mnt/user/appdata/keida-hub.

## Crafty Controller

Keida Hub does not require direct access to Crafty's server files for normal installation.

Advanced installations can optionally add a read-only Crafty server-files mapping when filesystem-backed console functionality is desired.

## Current status

Keida Hub is currently in beta.

This repository contains installation material only. The application source repository is separate and private.
