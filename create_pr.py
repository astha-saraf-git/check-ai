#!/usr/bin/env python3
import subprocess
import json

# Get GitHub token from git credential helper
try:
    result = subprocess.run(
        ["git", "credential-osxkeychain", "get"],
        input=b"host=github.com\n",
        capture_output=True,
        cwd="/Users/asthasaraf1/Desktop/check-ai"
    )
    
    credentials = {}
    for line in result.stdout.decode().split('\n'):
        if '=' in line:
            key, value = line.split('=', 1)
            credentials[key] = value
    
    token = credentials.get('password', '')
    
    if token:
        print(f"Token found: {token[:10]}...")
    else:
        print("No token found in keychain")
        
except Exception as e:
    print(f"Error: {e}")
