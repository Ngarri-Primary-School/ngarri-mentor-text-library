const encoder = new TextEncoder();
const embedded = __EMBEDDED_FILES__;

function loginPage(message = '') {
  const error = message ? `<p class="error" role="alert">${message}</p>` : '';
  return `<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Sign in | Ngarri Mentor Text Library</title><style>:root{font-family:system-ui,-apple-system,Segoe UI,sans-serif;color:#223630;background:#edf1e8}*{box-sizing:border-box}body{min-height:100vh;margin:0;display:grid;place-items:center;padding:24px}main{width:min(420px,100%);background:#fff;border:1px solid #d7e0d6;border-radius:8px;padding:32px;box-shadow:0 14px 50px #1834261a}.eyebrow{font-size:12px;font-weight:750;color:#4e6b5e}h1{font-family:Georgia,serif;font-size:30px;margin:10px 0 24px}label{display:block;font-weight:650;margin:16px 0 7px}input{width:100%;font:inherit;padding:12px;border:1px solid #aabdb0;border-radius:7px}button{width:100%;margin-top:22px;padding:12px;border:0;border-radius:7px;background:#326448;color:#fff;font:inherit;font-weight:700;cursor:pointer}.error{color:#8b2e25;background:#fff0ed;padding:10px;border-radius:6px}</style></head><body><main><span class="eyebrow">NGARRI PRIMARY SCHOOL</span><h1>Mentor Text Library</h1>${error}<form method="post" action="/login"><label for="username">Username</label><input id="username" name="username" autocomplete="username" required><label for="password">Password</label><input id="password" name="password" type="password" autocomplete="current-password" required><button type="submit">Sign in</button></form></main></body></html>`;
}

async function signature(secret) {
  const key = await crypto.subtle.importKey('raw', encoder.encode(secret), {name:'HMAC',hash:'SHA-256'}, false, ['sign']);
  const bytes = new Uint8Array(await crypto.subtle.sign('HMAC', key, encoder.encode('ngarri-library-session')));
  return btoa(String.fromCharCode(...bytes)).replaceAll('+','-').replaceAll('/','_').replaceAll('=','');
}

function cookieValue(request) {
  return request.headers.get('Cookie')?.match(/(?:^|;\s*)ngarri_session=([^;]+)/)?.[1] || '';
}

function equal(a,b) {
  const left=encoder.encode(a),right=encoder.encode(b);let diff=left.length^right.length;
  for(let i=0;i<Math.max(left.length,right.length);i++)diff|=(left[i%left.length]||0)^(right[i%right.length]||0);
  return diff===0;
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (!env.SITE_USERNAME || !env.SITE_PASSWORD) return new Response('Site access is not configured.', {status:503});
    if (url.pathname === '/login' && request.method === 'POST') {
      const form = await request.formData();
      if (equal(String(form.get('username')||''),env.SITE_USERNAME) && equal(String(form.get('password')||''),env.SITE_PASSWORD)) {
        return new Response(null,{status:303,headers:{Location:'/', 'Set-Cookie':`ngarri_session=${await signature(env.SITE_PASSWORD)}; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=28800`}});
      }
      return new Response(loginPage('The username or password was not recognised.'),{status:401,headers:{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-store'}});
    }
    if (url.pathname === '/logout') return new Response(null,{status:303,headers:{Location:'/login','Set-Cookie':'ngarri_session=; Path=/; HttpOnly; Secure; SameSite=Lax; Max-Age=0'}});
    if (!equal(cookieValue(request), await signature(env.SITE_PASSWORD))) return new Response(loginPage(),{status:401,headers:{'Content-Type':'text/html; charset=utf-8','Cache-Control':'no-store'}});
    const file = url.pathname === '/' ? '/index.html' : url.pathname;
    if (embedded[file] !== undefined) {
      const types = {'.html':'text/html; charset=utf-8','.js':'text/javascript; charset=utf-8','.css':'text/css; charset=utf-8','.json':'application/json; charset=utf-8'};
      const extension = Object.keys(types).find(ext => file.endsWith(ext));
      return new Response(embedded[file],{headers:{'Content-Type':types[extension]||'text/plain; charset=utf-8','Cache-Control':'no-store'}});
    }
    return env.ASSETS.fetch(request);
  }
};
