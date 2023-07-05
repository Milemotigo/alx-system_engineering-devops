#!/usr/bin/env python3
import yaml

bash_script = """
#!/usr/bin/env bash
# This script configures Nginx with a custom HTTP response header on a new Ubuntu machine

# Restart Nginx
sudo service nginx restart
"""

manifest = {
    "manifest.yml": [
        {
            "name": "Configure Nginx with custom HTTP response header",
            "tasks": [
                {
                    "name": "Update system packages",
                    "command": "apt-get update",
                    "become": True
                },
                {
                    "name": "Upgrade system packages",
                    "command": "apt-get upgrade -y",
                    "become": True
                },
                {
                    "name": "Install Nginx",
                    "command": "apt-get install -y nginx",
                    "become": True
                },
                {
                    "name": "Configure custom HTTP response header",
                    "command": "echo 'add_header X-Served-By $hostname;' | tee /etc/nginx/conf.d/custom_header.conf",
                    "become": True
                },
                {
                    "name": "Restart Nginx",
                    "service": {
                        "name": "nginx",
                        "state": "restarted"
                    },
                    "become": True
                }
            ]
        }
    ]
}

with open("manifest.yml", "w") as f:
    yaml.dump(manifest, f)
