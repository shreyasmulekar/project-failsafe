const fs = require('fs');

const html = fs.readFileSync('aditi_os_widget.html', 'utf8');

// Find all elements with "close" in their onclick or class or id
const lines = html.split('\n');
lines.forEach((line, idx) => {
  if (line.includes('closeModal') || (line.toLowerCase().includes('close') && line.includes('onclick'))) {
    console.log(`Line ${idx + 1}: ${line.trim()}`);
  }
});
