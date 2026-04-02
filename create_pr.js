const https = require('https');

// You need to provide your GitHub token
// For now, let's try to read it from environment or git config
const token = process.env.GITHUB_TOKEN || '';

if (!token) {
  console.log('ERROR: GITHUB_TOKEN environment variable not set');
  console.log('Please set your GitHub token: export GITHUB_TOKEN="your_token_here"');
  process.exit(1);
}

const data = JSON.stringify({
  title: 'Add empty file',
  body: 'This PR adds an empty file to the repository',
  head: 'add-empty-file',
  base: 'main'
});

const options = {
  hostname: 'api.github.com',
  port: 443,
  path: '/repos/astha-saraf-git/check-ai/pulls',
  method: 'POST',
  headers: {
    'Authorization': `token ${token}`,
    'Accept': 'application/vnd.github.v3+json',
    'Content-Type': 'application/json',
    'Content-Length': data.length,
    'User-Agent': 'Node.js'
  }
};

const req = https.request(options, (res) => {
  let responseData = '';
  
  res.on('data', (chunk) => {
    responseData += chunk;
  });
  
  res.on('end', () => {
    console.log(`Status: ${res.statusCode}`);
    console.log('Response:');
    console.log(JSON.stringify(JSON.parse(responseData), null, 2));
  });
});

req.on('error', (e) => {
  console.error(`Problem with request: ${e.message}`);
});

req.write(data);
req.end();
