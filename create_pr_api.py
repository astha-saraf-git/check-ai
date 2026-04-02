#!/usr/bin/env python3
import subprocess
import sys
import os

# Try to read GITHUB_TOKEN from environment
token = os.environ.get('GITHUB_TOKEN', '')

if not token:
    print("ERROR: GITHUB_TOKEN environment variable not set")
    print("Please provide your GitHub token")
    sys.exit(1)

# Create PR using GitHub API via curl
import json

pr_data = {
    "title": "Add empty file",
    "body": "This PR adds an empty file to the repository",
    "head": "add-empty-file",
    "base": "main"
}

curl_cmd = [
    'curl', '-X', 'POST',
    '-H', f'Authorization: token {token}',
    '-H', 'Accept: application/vnd.github.v3+json',
    '-H', 'Content-Type: application/json',
    'https://api.github.com/repos/astha-saraf-git/check-ai/pulls',
    '-d', json.dumps(pr_data)
]

print("Creating PR...")
result = subprocess.run(curl_cmd, capture_output=True, text=True)

print("Response:")
print(result.stdout)

if result.returncode != 0:
    print("Error:", result.stderr)
    sys.exit(1)

# Parse and display PR info
try:
    pr_response = json.loads(result.stdout)
    if 'html_url' in pr_response:
        print(f"\n✅ PR created successfully!")
        print(f"PR URL: {pr_response['html_url']}")
        print(f"PR Number: {pr_response['number']}")
except:
    pass
