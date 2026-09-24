const fs = require('fs');
const html = fs.readFileSync('aditi_os_widget.html', 'utf8');

const matches = [...html.matchAll(/(?:document|window|\b\w+)\.addEventListener\s*\(\s*['"]([^'"]+)['"]/g)];
console.log('Event listeners count:', matches.length);
matches.forEach(m => {
  console.log(`Listener: ${m[0]}`);
});
