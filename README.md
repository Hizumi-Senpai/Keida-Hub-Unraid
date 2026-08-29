# Keida Hub for Unraid

This repository provides the Unraid Docker template for Keida Hub.

Keida Hub is distributed as a public Docker image through GitHub Container Registry. No GitHub account, source-code checkout, Python installation, Node installation, or local build is required.

## Current supported beta

<!-- KEIDA_CURRENT_BETA_START -->
`0.2.0-beta.7`
<!-- KEIDA_CURRENT_BETA_END -->

The Unraid template follows `ghcr.io/hizumi-senpai/keida-hub:beta`, so new installs and normal updates receive the current supported beta automatically.

This repository intentionally documents the current install/update path rather than keeping upgrade instructions for every older beta. If a future release needs a special manual migration, it will be called out prominently here while that migration is relevant.

## Install on Unraid

### 1. Download the Keida Hub template

Open an Unraid terminal and run:

    curl -fsSL 'https://raw.githubusercontent.com/Hizumi-Senpai/Keida-Hub-Unraid/main/templates/keida-hub.xml' -o /boot/config/plugins/dockerMan/templates-user/my-keida-hub.xml

    chmod 600 /boot/config/plugins/dockerMan/templates-user/my-keida-hub.xml

### 2. Open the template

In the Unraid WebUI:

1. Open **Docker**.
2. Click **Add Container**.
3. Open the **Template** dropdown.
4. Select **keida-hub**.

If it does not appear immediately, refresh the Add Container page once.

### 3. Review the defaults

The template uses:

- Docker image: `ghcr.io/hizumi-senpai/keida-hub:beta`
- Network: `bridge`
- WebUI port: `8787`
- Appdata: `/mnt/user/appdata/keida-hub`
- Container config path: `/config`
- Privileged mode: disabled

If port `8787` is already in use, change only the host-side WebUI port.

### 4. Install

Click **Apply** and allow Unraid to download and start the container.

When installation finishes, open the Keida Hub WebUI and complete the first-run setup.

## Updating Keida Hub

Beta installations follow the `:beta` container tag.

When a new supported beta is published, use Unraid's normal Docker update flow to update the Keida Hub container. Configuration, the database, and application state remain outside the container under `/mnt/user/appdata/keida-hub` and are preserved across normal container updates.

For routine beta-to-beta updates, no version-specific upgrade procedure is maintained here. Any release that requires unusual manual steps will include a temporary **Special migration notice** in this README.

## Crafty Controller

Keida Hub does not require direct access to Crafty's server files for normal installation.

Advanced installations can optionally add a read-only Crafty server-files mapping when filesystem-backed console functionality is desired.

## Automatic beta-page sync

This public install repository checks the published `:beta` container image on a schedule. When the image reports a new beta version, the current-version marker above is updated automatically.

The application source repository remains separate and private.
