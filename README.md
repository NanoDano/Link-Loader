# Link Loader

This app runs a Flask web app that listens on a TCP
port for HTTPS connections.

## Setup

Generate a self-signed cert:

```bash
pip install pyopenssl
python gen_self_signed_cert.py
```

## Add to startup

For Windows, see: https://www.devdungeon.com/content/windows-run-script-startup

```
schtasks /create /tn "Star Link Loader Script" /sc onlogon /tr "cmd.exe /c pause"
```

or Run (Win+R) `shell:startup` and drop the Python script in there.

For Linux, see: https://www.devdungeon.com/content/creating-systemd-service-files
