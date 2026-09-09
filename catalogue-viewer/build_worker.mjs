import { readFileSync, writeFileSync } from 'node:fs';

const files = {};
for (const name of ['index.html','app.js','config.js','style.css','cover-status.json']) {
  files[`/${name}`] = readFileSync(`out/${name}`, 'utf8');
}
const source = readFileSync('worker.js','utf8').replace('__EMBEDDED_FILES__',JSON.stringify(files));
writeFileSync('dist/server/index.js',source);
