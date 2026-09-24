const fs = require('fs');
const html = fs.readFileSync('aditi_os_widget.html', 'utf8');
const formMatches = [...html.matchAll(/<form[\s\S]*?<\/form>/g)];
console.log('Forms found:', formMatches.length);
formMatches.forEach((f, i) => {
  const m = f[0].match(/id=["']([^"']+)["']/);
  console.log(`Form ${i}: id=${m ? m[1] : 'none'}`);
});
