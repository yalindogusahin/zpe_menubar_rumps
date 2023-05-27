# ZPE Menubar Rumps

This repository contains the ZPE Menubar Rumps project. It is a Python library that allows you to create macOS menubar applications using the Rumps framework.

## Prerequisites 

You need an tailscale network. You need to deploy tailscale to your nodegrid devices. To do that you can follow my instructions on nodegrid tailscale repo.

https://github.com/yalindogusahin/zpe_tailscale

## Installation

To install the ZPE Menubar Rumps library, you can use pip:

```bash
pip install zpe_menubar_rumps
```

## Usage

You need to change your tailscale informations on 'tailscale_api.py' script.

```
tailnet="YOUR_TAILNET_ID"
api_key="tskey-api-YOUR_TAILSCALE_API_KEY"
```

Then you can run your 'menubar_with_submenus.py' to start menu app.

