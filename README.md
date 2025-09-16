# Marimo Starter

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/pairspaces/marimo-starter)

## Features

- Minimal
- Dev Container integration

## Usage

### Setup

1. Using the PairSpaces CLI, create an authorization token. See [Container Spaces](https://docs.pairspaces.com/spaces/new/container) for more details.

    ```sh
    pair spaces authorize
    ```

2. Copy the token to your `devcontainer.json` in the following section.

    ```json
    {
        "features": {
            "ghcr.io/pairspaces/devcontainers/pairspaces": {
                "token": "TOKEN"
            }
        },
    }
    ```

3. Push the change to your repository (if using GitHub Codespaces).
4. Your team can join you by using the PairSpaces CLI to connect to your Codespace. See [Connecting to Shared Spaces](https://docs.pairspaces.com/spaces/sharing/sharing-spaces#connecting-to-shared-spaces) in our docs.

### VSCode

1. Open folder in VSCode.
2. Follow instructions to reopen the folder to develop in a container.
3. Open http://localhost:8080 to view the Marimo app.

### GitHub Codespaces

1. Click `Open in GitHub Codespaces` from the README page.
2. When the container is configured and running, click `Ports` from the console pane.
3. Open the forwarded port labeled `marimo-starter`.

![Marimo Starter Console Port](https://res.cloudinary.com/dojzxu4n2/image/upload/v1758059619/Marimo_Starter_Console_Port_xndtkz.png)
