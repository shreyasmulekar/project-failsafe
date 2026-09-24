const fs = require('fs');

const html = fs.readFileSync('aditi_os_widget.html', 'utf8');

// Let's parse all modals and check if their start and end tags match!
const lines = html.split('\n');

let currentModal = null;
let modalStartLine = 0;
let depth = 0;

for (let i = 0; i < lines.length; i++) {
  const line = lines[i];
  
  // Check modal start
  const match = line.match(/<div\s+id=["'](modal-[^"']+)["']/);
  if (match) {
    if (currentModal) {
      console.log(`WARNING: Nested or unclosed modal detected! Current: ${currentModal} (started line ${modalStartLine}), New: ${match[1]} at line ${i + 1}`);
    }
    currentModal = match[1];
    modalStartLine = i + 1;
    depth = 0;
  }

  if (currentModal) {
    // Count open div vs close div on this line
    const opens = (line.match(/<div\b/gi) || []).length;
    const closes = (line.match(/<\/div>/gi) || []).length;
    depth += (opens - closes);

    if (depth <= 0) {
      console.log(`Modal ${currentModal} (started line ${modalStartLine}) CLOSED at line ${i + 1} (depth: ${depth})`);
      currentModal = null;
    }
  }
}

if (currentModal) {
  console.log(`ERROR: Modal ${currentModal} started at line ${modalStartLine} NEVER CLOSED! (remaining depth: ${depth})`);
}
