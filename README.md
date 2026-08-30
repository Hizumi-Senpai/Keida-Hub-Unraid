# Keida Hub for Unraid

This repository provides the Unraid Docker template for Keida Hub.

Keida Hub is distributed as a public Docker image through GitHub Container Registry. No GitHub account, source-code checkout, Python installation, Node installation, or local build is required.

## Current supported beta

<!-- KEIDA_CURRENT_BETA_START -->
`0.2.0-beta.8`
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

## Optional Discord sign-in for your own Hub

Discord sign-in is portable, but each independent Keida Hub should use its own Discord application instead of sharing the credentials and redirect URI used by `keida.me`. Discord requires OAuth redirect URIs to be explicitly registered, and Keida intentionally does not publish or bake a shared client secret into the container.

### 1. Create a Discord application

In the Discord Developer Portal, create an application for your Hub and record its **Application ID / Client ID** and **Client Secret**.

Under the application's OAuth2 settings, add the exact callback URL for your Hub:

    https://your-keida-host.example/api/auth/discord/callback

Use the real public HTTPS address that users will open. The URI entered in Discord must exactly match the value configured in the Keida Hub template.

### 2. Store the client secret outside the Docker template

Keida reads the Discord OAuth client secret from `/config/discord-oauth-client-secret` so the secret does not appear in the Docker template or normal container environment listing.

On Unraid, create that file inside Keida's appdata directory:

    install -d -m 700 /mnt/user/appdata/keida-hub
    printf '%s\n' 'YOUR_DISCORD_CLIENT_SECRET' > /mnt/user/appdata/keida-hub/discord-oauth-client-secret
    chmod 600 /mnt/user/appdata/keida-hub/discord-oauth-client-secret

Do not commit this file or paste the client secret into GitHub issues, Discord, or the Unraid template.

### 3. Configure the advanced Unraid fields

Edit the Keida Hub container, enable **Show more settings**, and set:

- **Discord Sign-In Enabled:** `true`
- **Discord OAuth Client ID:** your Discord Application ID
- **Discord OAuth Redirect URI:** the exact callback URI registered above
- **Discord Guild ID:** the Discord server whose members are allowed to sign in

Apply the container changes. Keida requests only the Discord identity and guild-membership scopes needed for login, verifies membership in the configured server, and creates the normal Keida user session after a successful sign-in.

If these values are incomplete or the client-secret file is missing, Discord sign-in stays unavailable instead of falling back to another installation's credentials.

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
