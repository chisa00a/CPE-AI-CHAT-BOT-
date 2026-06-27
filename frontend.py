# frontend.py — CPE AI v5

_FONTS = (
    '<link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;600;700'
    '&family=Prompt:wght@400;600;700&display=swap" rel="stylesheet">'
    '<link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">'
)

_BASE_CSS = """<style>
:root{
  --bg:#F0F4F8;--panel:#fff;--text:#1A202C;--muted:#718096;--line:#E2E8F0;
  --accent:#FF6B00;--accent2:#FF9A3C;
  --success:#10B981;--danger:#EF4444;--warn:#F59E0B;--info:#3B82F6;
  --shadow:0 4px 20px rgba(0,0,0,.08);--shadow-lg:0 8px 40px rgba(0,0,0,.12);
  --radius:14px;
}
[data-theme="dark"]{
  --bg:#0F1117;--panel:#1A1D27;--text:#E2E8F0;--muted:#8892A4;--line:#2D3348;
  --shadow:0 4px 20px rgba(0,0,0,.35);--shadow-lg:0 8px 40px rgba(0,0,0,.5);
}
*{box-sizing:border-box;font-family:'Sarabun',sans-serif;margin:0;padding:0;}
html,body{height:100%;background:var(--bg);color:var(--text);overflow-x:hidden;transition:background .25s,color .25s;}
a{color:var(--accent);text-decoration:none;font-weight:600;}
a:hover{text-decoration:underline;}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;
     padding:10px 18px;border-radius:10px;border:none;cursor:pointer;
     background:linear-gradient(135deg,var(--accent),var(--accent2));
     color:#fff;font-weight:700;font-family:'Sarabun',sans-serif;font-size:14px;
     box-shadow:0 4px 14px rgba(255,107,0,.3);transition:all .2s;}
.btn:hover{transform:translateY(-1px);box-shadow:0 6px 20px rgba(255,107,0,.4);}
.btn:active{transform:none;}
.btn2{background:#EDF2F7;color:#4A5568;box-shadow:none;border:1px solid var(--line);}
[data-theme="dark"] .btn2{background:#2D3348;color:#CBD5E0;border-color:#3D4563;}
.btn2:hover{background:#E2E8F0;color:#1A202C;box-shadow:none;transform:none;}
[data-theme="dark"] .btn2:hover{background:#3D4563;color:#E2E8F0;}
.btn-sm{padding:6px 12px;font-size:12px;border-radius:8px;}
.btn-danger{background:linear-gradient(135deg,#EF4444,#F87171);box-shadow:0 4px 14px rgba(239,68,68,.3);}
.btn-success{background:linear-gradient(135deg,#10B981,#34D399);box-shadow:0 4px 14px rgba(16,185,129,.3);}
.inp,textarea,select{width:100%;padding:12px 14px;border-radius:10px;
  border:1.5px solid var(--line);background:var(--panel);color:var(--text);
  outline:none;font-family:'Sarabun',sans-serif;font-size:14px;transition:all .2s;}
.inp:focus,textarea:focus,select:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(255,107,0,.12);}
.card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:20px;}
.stat-card{background:var(--panel);border:1px solid var(--line);border-radius:var(--radius);
           box-shadow:var(--shadow);padding:20px 24px;display:flex;align-items:center;gap:16px;}
.stat-icon{width:52px;height:52px;border-radius:12px;display:flex;align-items:center;
           justify-content:center;font-size:22px;flex-shrink:0;}
hr{border:none;border-top:1px solid var(--line);margin:15px 0;}
.badge{display:inline-flex;align-items:center;gap:4px;padding:3px 10px;border-radius:20px;
       background:#FFF4EA;color:#CC4E00;font-size:11px;font-weight:700;border:1px solid #FFD4A8;}
[data-theme="dark"] .badge{background:#2A1A00;color:#FF9A3C;border-color:#5C3200;}
.badge-green{background:#ECFDF5;color:#065F46;border-color:#A7F3D0;}
[data-theme="dark"] .badge-green{background:#052E1C;color:#34D399;border-color:#065F46;}
.badge-blue{background:#EFF6FF;color:#1E40AF;border-color:#BFDBFE;}
[data-theme="dark"] .badge-blue{background:#0C1A3A;color:#60A5FA;border-color:#1E40AF;}
.hide{display:none!important;}
.modalBack{position:fixed;inset:0;background:rgba(15,23,42,.6);
           display:flex;align-items:center;justify-content:center;
           z-index:200;backdrop-filter:blur(6px);animation:fadeIn .2s ease;}
.modal{width:min(980px,96%);background:var(--panel);border-radius:var(--radius);
       padding:28px;box-shadow:var(--shadow-lg);max-height:88vh;overflow-y:auto;color:var(--text);}
.modalGrid{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px;}
table{width:100%;border-collapse:collapse;font-size:13px;}
th{padding:10px 12px;background:var(--bg);border-bottom:2px solid var(--line);
   font-weight:700;color:var(--muted);text-transform:uppercase;font-size:11px;letter-spacing:.5px;}
td{padding:10px 12px;border-bottom:1px solid var(--line);vertical-align:top;color:var(--text);}
tr:hover td{background:var(--bg);}
.toast{position:fixed;bottom:24px;right:24px;background:#1A202C;color:#fff;
       padding:12px 20px;border-radius:10px;font-size:13px;font-weight:600;
       box-shadow:var(--shadow-lg);z-index:999;animation:slideUp .3s ease;}
[data-theme="dark"] .toast{background:#E2E8F0;color:#1A202C;}
.dots span{display:inline-block;width:7px;height:7px;border-radius:50%;
           background:var(--accent);margin:0 2px;animation:bounce 1.2s infinite;}
.dots span:nth-child(2){animation-delay:.2s;}
.dots span:nth-child(3){animation-delay:.4s;}
.upload-zone{border:2px dashed var(--line);border-radius:12px;padding:36px 20px;
             text-align:center;cursor:pointer;transition:all .2s;color:var(--muted);}
.upload-zone:hover,.upload-zone.drag{border-color:var(--accent);background:#FFF9F5;color:var(--accent);}
[data-theme="dark"] .upload-zone:hover,[data-theme="dark"] .upload-zone.drag{background:#1F120A;color:var(--accent);}
.progress-wrap{width:100%;height:10px;background:var(--line);border-radius:5px;overflow:hidden;margin-top:10px;}
.progress-bar{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));
              border-radius:5px;transition:width .4s ease;width:0%;}
/* Theme toggle button */
.theme-toggle{width:36px;height:36px;border-radius:9px;border:1.5px solid var(--line);
              background:var(--panel);color:var(--text);cursor:pointer;
              display:flex;align-items:center;justify-content:center;font-size:16px;
              transition:all .2s;flex-shrink:0;}
.theme-toggle:hover{border-color:var(--accent);color:var(--accent);background:var(--bg);}
@keyframes slideUp{from{opacity:0;transform:translateY(10px);}to{opacity:1;transform:translateY(0);}}
@keyframes fadeIn{from{opacity:0;}to{opacity:1;}}
@keyframes bounce{0%,80%,100%{transform:translateY(0);}40%{transform:translateY(-8px);}}
@keyframes msgIn{from{opacity:0;transform:translateY(6px);}to{opacity:1;transform:translateY(0);}}
</style>"""

# Script สำหรับ Dark Mode (ใส่ใน <head> ก่อน CSS เพื่อป้องกัน flash)
_THEME_SCRIPT = """<script>
(function(){
  var t=localStorage.getItem('cpe_theme')||'light';
  if(t==='dark') document.documentElement.setAttribute('data-theme','dark');
})();
function toggleTheme(){
  var isDark=document.documentElement.getAttribute('data-theme')==='dark';
  var next=isDark?'light':'dark';
  document.documentElement.setAttribute('data-theme',next);
  localStorage.setItem('cpe_theme',next);
  var btn=document.getElementById('themeBtn');
  if(btn) btn.innerHTML=next==='dark'?'<i class="fas fa-sun"></i>':'<i class="fas fa-moon"></i>';
}
</script>"""


def _theme_btn():
    """ปุ่ม toggle dark/light mode"""
    return ('<button class="theme-toggle" id="themeBtn" onclick="toggleTheme()" '
            'title="เปลี่ยนธีม">'
            '<i class="fas fa-moon"></i>'
            '</button>'
            '<script>'
            '(function(){'
            'var isDark=document.documentElement.getAttribute("data-theme")==="dark";'
            'var btn=document.getElementById("themeBtn");'
            'if(btn && isDark) btn.innerHTML=\'<i class="fas fa-sun"></i>\';'
            '})();'
            '</script>')


def _shell(title, body):
    return (
        '<!doctype html><html lang="th"><head><meta charset="utf-8"/>'
        '<meta name="viewport" content="width=device-width,initial-scale=1"/>'
        '<title>' + title + ' \u2014 CPE AI v5</title>'
        + _THEME_SCRIPT + _FONTS + _BASE_CSS +
        '</head><body>' + body + '</body></html>'
    )


def login_page(error=""):
    err = ""
    if error:
        err = ("<div style='color:#C53030;margin-bottom:14px;background:#FFF5F5;"
               "padding:12px 16px;border-radius:8px;border-left:3px solid #FC8181;font-size:14px;'>"
               "<i class='fas fa-exclamation-circle'></i> " + error + "</div>")
    body = """
<div style="min-height:100vh;display:flex;align-items:center;justify-content:center;
            background:linear-gradient(135deg,#FFF4EA 0%,#F0F4F8 60%,#EBF4FF 100%);">
  <div style="position:fixed;top:16px;right:16px;">""" + _theme_btn() + """</div>
  <div style="width:100%;max-width:420px;padding:20px;">
    <div class="card" style="border-top:4px solid var(--accent);">
      <div style="text-align:center;padding:10px 0 20px;">
        <div style="width:72px;height:72px;border-radius:20px;
                    background:linear-gradient(135deg,var(--accent),var(--accent2));
                    display:flex;align-items:center;justify-content:center;
                    margin:0 auto 14px;box-shadow:0 8px 24px rgba(255,107,0,.3);">
          <i class="fas fa-robot" style="font-size:32px;color:#fff;"></i>
        </div>
        <div style="font-family:'Prompt',sans-serif;font-size:22px;font-weight:700;color:var(--accent);">
          CPE AI Assistant</div>
        <div style="font-size:13px;color:var(--muted);margin-top:4px;">
          v5 Free &middot; Gemini Flash + Groq &middot; RAG Hybrid</div>
      </div>
      <hr/>""" + err + """
      <form method="post" action="/login">
        <label style="font-size:13px;font-weight:700;color:var(--muted);display:block;margin-bottom:6px;">
          <i class="fas fa-user"></i> ชื่อผู้ใช้</label>
        <input class="inp" name="username" required style="margin-bottom:14px;" placeholder="กรอกชื่อผู้ใช้"/>
        <label style="font-size:13px;font-weight:700;color:var(--muted);display:block;margin-bottom:6px;">
          <i class="fas fa-lock"></i> รหัสผ่าน</label>
        <input class="inp" name="password" type="password" required
               style="margin-bottom:20px;" placeholder="กรอกรหัสผ่าน"/>
        <button class="btn" type="submit" style="width:100%;font-size:15px;padding:13px;">
          <i class="fas fa-sign-in-alt"></i> เข้าสู่ระบบ</button>
      </form>
      <div style="text-align:center;margin-top:14px;font-size:13px;color:var(--muted);">
        ยังไม่มีบัญชี? <a href="/register">สมัครสมาชิก</a></div>
    </div>
  </div>
</div>"""
    return _shell("เข้าสู่ระบบ", body)


def register_page(error="", success=""):
    msg = ""
    if error:
        msg = ("<div style='color:#C53030;margin-bottom:14px;background:#FFF5F5;"
               "padding:12px 16px;border-radius:8px;border-left:3px solid #FC8181;font-size:14px;'>"
               "<i class='fas fa-exclamation-circle'></i> " + error + "</div>")
    if success:
        msg = ("<div style='color:#065F46;margin-bottom:14px;background:#ECFDF5;"
               "padding:12px 16px;border-radius:8px;border-left:3px solid #6EE7B7;font-size:14px;'>"
               "<i class='fas fa-check-circle'></i> " + success + "</div>")
    body = """
<div style="min-height:100vh;display:flex;align-items:center;justify-content:center;
            background:linear-gradient(135deg,#FFF4EA 0%,#F0F4F8 60%,#EBF4FF 100%);">
  <div style="position:fixed;top:16px;right:16px;">""" + _theme_btn() + """</div>
  <div style="width:100%;max-width:440px;padding:20px;">
    <div class="card" style="border-top:4px solid var(--info);">
      <div style="text-align:center;padding:8px 0 16px;">
        <div style="font-family:'Prompt',sans-serif;font-size:20px;font-weight:700;color:#1E40AF;">
          <i class="fas fa-user-plus"></i> สมัครสมาชิก CPE AI</div>
      </div>
      <hr/>""" + msg + """
      <form method="post" action="/register">
        <label style="font-size:13px;font-weight:700;color:var(--muted);display:block;margin-bottom:6px;">ชื่อผู้ใช้</label>
        <input class="inp" name="username" required style="margin-bottom:12px;" placeholder="อย่างน้อย 3 ตัวอักษร"/>
        <label style="font-size:13px;font-weight:700;color:var(--muted);display:block;margin-bottom:6px;">อีเมล (ไม่บังคับ)</label>
        <input class="inp" name="email" type="email" style="margin-bottom:12px;" placeholder="your@email.com"/>
        <label style="font-size:13px;font-weight:700;color:var(--muted);display:block;margin-bottom:6px;">รหัสผ่าน</label>
        <input class="inp" name="password" type="password" required style="margin-bottom:12px;" placeholder="อย่างน้อย 6 ตัวอักษร"/>
        <label style="font-size:13px;font-weight:700;color:var(--muted);display:block;margin-bottom:6px;">ยืนยันรหัสผ่าน</label>
        <input class="inp" name="confirm" type="password" required style="margin-bottom:20px;" placeholder="พิมพ์รหัสผ่านอีกครั้ง"/>
        <button class="btn btn-success" type="submit" style="width:100%;font-size:15px;padding:13px;">
          <i class="fas fa-user-plus"></i> สมัครสมาชิก</button>
      </form>
      <div style="text-align:center;margin-top:14px;font-size:13px;color:var(--muted);">
        มีบัญชีแล้ว? <a href="/">เข้าสู่ระบบ</a></div>
    </div>
  </div>
</div>"""
    return _shell("สมัครสมาชิก", body)


def dashboard_page(username, role):
    body = """
<div style="min-height:100vh;background:var(--bg);">
  <div style="background:var(--panel);border-bottom:1px solid var(--line);padding:14px 28px;
              display:flex;justify-content:space-between;align-items:center;
              box-shadow:0 2px 8px rgba(0,0,0,.04);position:sticky;top:0;z-index:50;">
    <div style="display:flex;gap:12px;align-items:center;">
      <div style="width:40px;height:40px;border-radius:10px;
                  background:linear-gradient(135deg,var(--accent),var(--accent2));
                  display:flex;align-items:center;justify-content:center;">
        <i class="fas fa-chart-line" style="color:#fff;font-size:18px;"></i></div>
      <div>
        <div style="font-family:'Prompt',sans-serif;font-weight:700;font-size:17px;">Admin Dashboard</div>
        <div style="font-size:12px;color:var(--muted);">ผู้ดูแล: <b>""" + username + """</b></div>
      </div>
    </div>
    <div style="display:flex;gap:8px;align-items:center;">""" + _theme_btn() + """
      <button class="btn btn2 btn-sm" onclick="location.href='/chat'">
        <i class="fas fa-comments"></i> กลับแชท</button>
      <button class="btn btn-danger btn-sm" onclick="location.href='/logout'">
        <i class="fas fa-sign-out-alt"></i> ออก</button>
    </div>
  </div>
  <div style="max-width:1200px;margin:0 auto;padding:28px 20px;">
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:16px;margin-bottom:24px;">
      <div class="stat-card">
        <div class="stat-icon" style="background:#FFF4EA;">
          <i class="fas fa-brain" style="color:var(--accent);"></i></div>
        <div><div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;">ฐานความรู้</div>
          <div id="s_kb" style="font-size:28px;font-weight:700;color:var(--accent);">—</div></div>
      </div>
      <div class="stat-card">
        <div class="stat-icon" style="background:#EFF6FF;">
          <i class="fas fa-users" style="color:var(--info);"></i></div>
        <div><div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;">ผู้ใช้งาน</div>
          <div id="s_users" style="font-size:28px;font-weight:700;color:var(--info);">—</div></div>
      </div>
      <div class="stat-card">
        <div class="stat-icon" style="background:#ECFDF5;">
          <i class="fas fa-comments" style="color:var(--success);"></i></div>
        <div><div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;">การสนทนา</div>
          <div id="s_logs" style="font-size:28px;font-weight:700;color:var(--success);">—</div></div>
      </div>
      <div class="stat-card">
        <div class="stat-icon" style="background:#FFF9EC;">
          <i class="fas fa-star" style="color:var(--warn);"></i></div>
        <div><div style="font-size:11px;color:var(--muted);font-weight:700;text-transform:uppercase;">Feedback</div>
          <div id="s_fb" style="font-size:15px;font-weight:700;color:var(--warn);margin-top:4px;">—</div></div>
      </div>
    </div>
    <div class="card">
      <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;">
        <b style="font-size:15px;"><i class="fas fa-history" style="color:var(--accent);"></i> ประวัติล่าสุด</b>
        <button class="btn btn2 btn-sm" onclick="loadStats()">
          <i class="fas fa-sync-alt"></i> รีเฟรช</button>
      </div>
      <div style="overflow-x:auto;">
        <table>
          <thead><tr><th>เวลา</th><th>ผู้ใช้</th><th>คำถาม</th><th>คำตอบ AI</th></tr></thead>
          <tbody id="logs_tbody"></tbody>
        </table>
      </div>
    </div>
  </div>
</div>
<script>
async function loadStats(){
  const d=await(await fetch('/api/stats')).json();
  document.getElementById('s_kb').textContent=d.total_kb+' ข้อ';
  document.getElementById('s_users').textContent=d.total_users+' คน';
  document.getElementById('s_logs').textContent=d.total_logs+' ครั้ง';
  document.getElementById('s_fb').innerHTML=
    '<span style="color:var(--success)">👍 '+d.likes+'</span>&nbsp;'+
    '<span style="color:var(--danger)">👎 '+d.dislikes+'</span>';
  const tb=document.getElementById('logs_tbody');
  tb.innerHTML='';
  (d.recent_logs||[]).forEach(r=>{
    const tr=document.createElement('tr');
    tr.innerHTML='<td style="white-space:nowrap;font-size:12px;color:var(--muted)">'+r.ts.slice(0,16)+'</td>'+
      '<td><b>'+r.username+'</b></td>'+
      '<td style="max-width:230px;">'+r.question+'</td>'+
      '<td style="max-width:350px;color:var(--muted);font-size:13px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">'+r.answer+'</td>';
    tb.appendChild(tr);
  });
}
loadStats();
</script>"""
    return _shell("Dashboard", body)


def chat_page(username, role):
    is_admin = "true" if role == "admin" else "false"
    upload_display = "flex" if role == "admin" else "none"

    # CSS แยกออกมาเป็น string ธรรมดา ไม่ใช้ f-string
    chat_css = """<style>
.app{height:100vh;display:flex;overflow:hidden;}
.sidebar{width:286px;min-width:286px;background:var(--panel);border-right:1px solid var(--line);
         display:flex;flex-direction:column;overflow:hidden;transition:background .25s;}
.sidebar-header{padding:16px 16px 12px;border-bottom:1px solid var(--line);}
.brand-logo{width:42px;height:42px;border-radius:12px;flex-shrink:0;
            background:linear-gradient(135deg,var(--accent),var(--accent2));
            display:flex;align-items:center;justify-content:center;}
.thread-list{flex:1;overflow-y:auto;padding:6px 0;}
.threadItem{padding:10px 14px;border-radius:10px;cursor:pointer;font-size:14px;
            color:var(--muted);transition:all .15s;display:flex;align-items:center;
            gap:8px;margin:2px 8px;}
.threadItem:hover{background:#FFF4EA;color:var(--accent);}
[data-theme="dark"] .threadItem:hover{background:#2A1400;}
.threadItem.active{background:#FFF4EA;color:var(--accent);font-weight:700;}
[data-theme="dark"] .threadItem.active{background:#2A1400;}
.nav-item{padding:10px 14px;margin:2px 8px;border-radius:10px;cursor:pointer;
          font-size:14px;display:flex;align-items:center;gap:10px;
          transition:all .15s;color:var(--muted);}
.nav-item:hover{background:var(--bg);}
.sidebar-footer{padding:10px 8px;border-top:1px solid var(--line);}
.main{flex:1;display:flex;flex-direction:column;background:var(--bg);overflow:hidden;transition:background .25s;}
.topbar{padding:14px 24px;border-bottom:1px solid var(--line);
        display:flex;justify-content:space-between;align-items:center;
        background:var(--panel);box-shadow:0 2px 8px rgba(0,0,0,.04);}
.chat{flex:1;overflow-y:auto;padding:24px;display:flex;flex-direction:column;gap:4px;}
.msg{display:flex;gap:12px;max-width:84%;align-items:flex-end;animation:msgIn .25s ease;}
.msg.user{align-self:flex-end;flex-direction:row-reverse;margin-left:auto;}
.av{width:36px;height:36px;border-radius:50%;display:flex;align-items:center;
    justify-content:center;font-weight:700;font-size:14px;flex-shrink:0;}
.bot .av{background:linear-gradient(135deg,var(--accent),var(--accent2));
         color:#fff;box-shadow:0 3px 10px rgba(255,107,0,.3);}
.user .av{background:#DBEAFE;color:#1D4ED8;}
.bubble{padding:13px 17px;border-radius:16px;line-height:1.7;
        font-size:14.5px;max-width:100%;box-shadow:0 2px 10px rgba(0,0,0,.06);}
.bot .bubble{background:var(--panel);border:1px solid var(--line);border-bottom-left-radius:4px;color:var(--text);}
.user .bubble{background:linear-gradient(135deg,#3B82F6,#60A5FA);
              color:#fff;border:none;border-bottom-right-radius:4px;}
.fb-row{display:flex;gap:6px;margin-top:8px;}
.fb-btn{border:none;background:none;cursor:pointer;font-size:18px;
        padding:2px 4px;opacity:.35;transition:all .15s;}
.fb-btn:hover{opacity:1;transform:scale(1.2);}
.fb-btn.active{opacity:1;}
.src-row{display:flex;gap:5px;flex-wrap:wrap;margin-top:7px;}
.src-tag{font-size:11px;padding:2px 8px;border-radius:5px;
         background:var(--bg);border:1px solid var(--line);color:var(--muted);}
.composer{padding:14px 18px;background:var(--panel);border-top:1px solid var(--line);
          box-shadow:0 -4px 20px rgba(0,0,0,.04);}
.tip-box{background:#FFFBF0;border:1px dashed #FCD34D;border-radius:8px;
         padding:7px 12px;margin-bottom:10px;font-size:12px;color:#92400E;line-height:1.6;}
[data-theme="dark"] .tip-box{background:#1C1500;border-color:#5C4200;color:#D4A017;}
.composer-row{display:flex;gap:10px;align-items:flex-end;}
.composer textarea{height:52px;resize:none;flex:1;border-radius:12px;
                   border:1.5px solid var(--line);padding:14px 16px;font-size:14px;
                   font-family:'Sarabun',sans-serif;line-height:1.5;transition:all .2s;
                   background:var(--panel);color:var(--text);}
.composer textarea:focus{border-color:var(--accent);box-shadow:0 0 0 3px rgba(255,107,0,.1);}
.send-btn{width:52px;height:52px;border-radius:14px;flex-shrink:0;
          background:linear-gradient(135deg,var(--accent),var(--accent2));
          border:none;color:#fff;font-size:20px;cursor:pointer;
          box-shadow:0 4px 14px rgba(255,107,0,.35);transition:all .2s;
          display:flex;align-items:center;justify-content:center;}
.send-btn:hover{transform:translateY(-1px);box-shadow:0 6px 20px rgba(255,107,0,.45);}
</style>"""

    # HTML แยกออกมา ไม่ใช้ f-string ใช้ string concatenation แทน
    body = chat_css + """
<div class="app">
  <div class="sidebar">
    <div class="sidebar-header">
      <div style="display:flex;gap:12px;align-items:center;">
        <div class="brand-logo">
          <i class="fas fa-robot" style="font-size:20px;color:#fff;"></i></div>
        <div>
          <div style="font-family:'Prompt',sans-serif;font-weight:700;font-size:15px;color:var(--accent);">
            CPE AI v5</div>
          <div style="font-size:11px;color:var(--muted);">ยินดีต้อนรับ <b>""" + username + """</b></div>
        </div>
      </div>
    </div>
    <div style="padding:10px 8px 4px;">
      <button class="btn btn-sm" onclick="newThread()" style="width:100%;justify-content:center;">
        <i class="fas fa-plus"></i> สนทนาใหม่</button>
    </div>
    <div style="padding:12px 18px 4px;font-size:11px;font-weight:700;
                color:var(--muted);text-transform:uppercase;letter-spacing:.5px;">ประวัติแชท</div>
    <div class="thread-list" id="threadList"></div>
    <div class="sidebar-footer">
      <div class="nav-item" onclick="openKBModal()">
        <i class="fas fa-brain" style="color:var(--accent);"></i><span>จัดการฐานความรู้</span></div>
      <div class="nav-item" id="uploadNav" style="display:""" + upload_display + """;" onclick="openUploadModal()">
        <i class="fas fa-file-upload" style="color:var(--info);"></i><span>อัปโหลด PDF / DOCX</span></div>
      <div class="nav-item" onclick="location.href='/dashboard'">
        <i class="fas fa-chart-bar" style="color:var(--success);"></i><span>แดชบอร์ด</span></div>
      <div class="nav-item" onclick="toggleTheme()" style="cursor:pointer;">
        <i class="fas fa-circle-half-stroke" style="color:var(--warn);"></i>
        <span id="themeLabel">เปลี่ยนธีม</span></div>
      <div class="nav-item" onclick="location.href='/logout'" style="color:var(--danger);">
        <i class="fas fa-sign-out-alt" style="color:var(--danger);"></i><span>ออกจากระบบ</span></div>
    </div>
  </div>

  <div class="main">
    <div class="topbar">
      <div style="display:flex;align-items:center;gap:10px;">
        <i class="fas fa-comment-dots" style="color:var(--accent);font-size:18px;"></i>
        <b id="threadTitle" style="font-size:16px;">เลือกหัวข้อหรือสร้างแชทใหม่</b>
      </div>
      <div style="display:flex;gap:8px;align-items:center;">
        <span class="badge badge-green"><i class="fas fa-circle" style="font-size:8px;"></i> AI Online</span>
        <span class="badge badge-blue">Gemini Flash + Groq v5</span>
        <button class="theme-toggle" id="themeBtn" onclick="toggleTheme()" title="เปลี่ยนธีม">
          <i class="fas fa-moon"></i></button>
      </div>
    </div>
    <div class="chat" id="chat">
      <div style="text-align:center;padding:60px 20px;color:var(--muted);">
        <i class="fas fa-robot" style="font-size:52px;color:#FFD0A8;margin-bottom:16px;"></i>
        <div style="font-size:17px;font-weight:600;margin-bottom:8px;">สวัสดีครับ!</div>
        <div style="font-size:14px;line-height:1.8;">กด <b>+ สนทนาใหม่</b> เพื่อเริ่มต้นครับ</div>
      </div>
    </div>
    <div class="composer">
      <div class="tip-box">
        <i class="fas fa-lightbulb" style="color:var(--warn);"></i>
        <b>เคล็ดลับ:</b> ถามเรื่องหลักสูตร ค่าเทอม การรับสมัคร ทุนการศึกษา
        <span id="adminTip" class="hide"> |
          Admin: <code>สอน: คำถาม = คำตอบ</code> |
          <code>เรียนรู้เว็บ: URL</code></span>
      </div>
      <div class="composer-row">
        <textarea id="q" placeholder="พิมพ์คำถามที่นี่... (Enter ส่ง, Shift+Enter ขึ้นบรรทัด)"
          onkeydown="if(event.key==='Enter'&&!event.shiftKey){event.preventDefault();send();}">
        </textarea>
        <button class="send-btn" onclick="send()">
          <i class="fas fa-paper-plane"></i></button>
      </div>
    </div>
  </div>
</div>

<!-- KB MODAL -->
<div id="kbModal" class="modalBack hide">
  <div class="modal">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
      <b style="font-size:17px;"><i class="fas fa-brain" style="color:var(--accent);"></i> จัดการฐานความรู้ AI</b>
      <button class="btn btn2 btn-sm" onclick="closeKBModal()"><i class="fas fa-times"></i> ปิด</button>
    </div>
    <hr/>
    <div class="modalGrid">
      <div>
        <div style="font-weight:700;margin-bottom:12px;color:var(--accent);">
          <i class="fas fa-plus-circle"></i> เพิ่ม / แก้ไขข้อมูล</div>
        <input type="hidden" id="kb_id" value="0"/>
        <label style="font-size:12px;color:var(--muted);font-weight:700;">คำถาม / หัวข้อ</label>
        <input id="kb_q" class="inp" placeholder="เช่น: ค่าเทอมเท่าไหร่" style="margin:6px 0 12px;"/>
        <label style="font-size:12px;color:var(--muted);font-weight:700;">คำตอบ</label>
        <textarea id="kb_a" class="inp" placeholder="ใส่ข้อมูลคำตอบ"
                  style="margin:6px 0 12px;height:100px;"></textarea>
        <label style="font-size:12px;color:var(--muted);font-weight:700;">แท็ก (คั่นด้วย ,)</label>
        <input id="kb_t" class="inp" placeholder="เช่น: ทุน, รับสมัคร" style="margin:6px 0 16px;"/>
        <div style="display:flex;gap:8px;">
          <button class="btn" onclick="kbSave()" style="flex:1;"><i class="fas fa-save"></i> บันทึก</button>
          <button class="btn btn2" onclick="kbClear()"><i class="fas fa-eraser"></i> ล้าง</button>
        </div>
      </div>
      <div>
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;">
          <b style="color:var(--accent);"><i class="fas fa-list"></i> รายการ KB</b>
          <span id="kbCount" class="badge">0</span>
        </div>
        <input id="kbSearch" class="inp" placeholder="🔍 ค้นหา..." style="margin-bottom:10px;"
               oninput="filterKB(this.value)"/>
        <div id="kbList" style="max-height:340px;overflow-y:auto;
                                display:flex;flex-direction:column;gap:8px;"></div>
      </div>
    </div>
  </div>
</div>

<!-- UPLOAD MODAL -->
<div id="uploadModal" class="modalBack hide">
  <div class="modal" style="max-width:500px;">
    <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;">
      <b style="font-size:17px;"><i class="fas fa-file-upload" style="color:var(--info);"></i> อัปโหลดไฟล์เข้า KB</b>
      <button class="btn btn2 btn-sm" onclick="closeUploadModal()"><i class="fas fa-times"></i> ปิด</button>
    </div>
    <hr/>
    <div class="upload-zone" id="dropZone"
         onclick="document.getElementById('fileInput').click()"
         ondragover="event.preventDefault();this.classList.add('drag')"
         ondragleave="this.classList.remove('drag')"
         ondrop="handleDrop(event)">
      <i class="fas fa-cloud-upload-alt" style="font-size:44px;margin-bottom:12px;display:block;"></i>
      <div style="font-size:15px;font-weight:600;margin-bottom:6px;">คลิกหรือลากไฟล์มาวาง</div>
      <div style="font-size:13px;">รองรับ PDF และ DOCX (ไม่เกิน 15MB)</div>
    </div>
    <input type="file" id="fileInput" accept=".pdf,.docx" class="hide"
           onchange="startUpload(this.files[0])"/>
    <div id="uploadProgress" class="hide" style="margin-top:14px;">
      <div style="font-size:13px;font-weight:600;margin-bottom:6px;" id="uploadProgressText">
        กำลังอัปโหลด...</div>
      <div class="progress-wrap">
        <div class="progress-bar" id="progressBar"></div>
      </div>
    </div>
    <div id="uploadResult" style="display:none;margin-top:14px;border-radius:10px;
                                   padding:20px;text-align:center;"></div>
    <div style="text-align:center;margin-top:12px;">
      <button class="btn btn2 btn-sm hide" id="cancelBtn" onclick="cancelUpload()">
        <i class="fas fa-times"></i> ยกเลิก</button>
    </div>
  </div>
</div>
""" + """
<script>
var IS_ADMIN = """ + is_admin + """;
var _uploadCtrl = null;
var _pollTimer  = null;
var allKBItems  = [];
var currentThread = null;

if(IS_ADMIN) document.getElementById('adminTip').classList.remove('hide');

// ── Sync theme icon on load ──────────────────────────────────
(function(){
  var isDark=document.documentElement.getAttribute('data-theme')==='dark';
  var btn=document.getElementById('themeBtn');
  if(btn) btn.innerHTML=isDark?'<i class="fas fa-sun"></i>':'<i class="fas fa-moon"></i>';
  var lbl=document.getElementById('themeLabel');
  if(lbl) lbl.textContent=isDark?'โหมดสว่าง':'โหมดมืด';
})();

// ── Override toggleTheme to also update sidebar label ────────
var _origToggle=window.toggleTheme;
window.toggleTheme=function(){
  _origToggle();
  var isDark=document.documentElement.getAttribute('data-theme')==='dark';
  var btn=document.getElementById('themeBtn');
  if(btn) btn.innerHTML=isDark?'<i class="fas fa-sun"></i>':'<i class="fas fa-moon"></i>';
  var lbl=document.getElementById('themeLabel');
  if(lbl) lbl.textContent=isDark?'โหมดสว่าง':'โหมดมืด';
};

// ── Threads ─────────────────────────────────────────────────
async function loadThreads(){
  var d = await(await fetch('/api/threads')).json();
  var el = document.getElementById('threadList');
  el.innerHTML='';
  (d.items||[]).forEach(function(t){
    var div=document.createElement('div');
    div.className='threadItem'+(t.id===currentThread?' active':'');
    div.innerHTML='<i class="fas fa-comment" style="font-size:12px;opacity:.5;"></i>'+
      '<span style="flex:1;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">'+esc(t.title)+'</span>';
    div.onclick=function(){selectThread(t.id,t.title);};
    el.appendChild(div);
  });
}

async function newThread(){
  var title=prompt('ชื่อหัวข้อสนทนา:','คำถามทั่วไป');
  if(!title) return;
  var d=await(await fetch('/api/threads/create',{
    method:'POST',headers:{'Content-Type':'application/json'},
    body:JSON.stringify({title:title})
  })).json();
  await loadThreads();
  selectThread(d.id,title);
}

async function selectThread(id,title){
  currentThread=id;
  document.getElementById('threadTitle').textContent=title;
  await loadThreads();
  await loadHistory(id);
  document.getElementById('q').focus();
}

async function loadHistory(threadId){
  var chat=document.getElementById('chat');
  chat.innerHTML='<div style="text-align:center;padding:20px;color:var(--muted);">กำลังโหลด...</div>';
  var d=await(await fetch('/api/thread/history?thread_id='+threadId)).json();
  chat.innerHTML='';
  if(!d.items||!d.items.length){
    chat.innerHTML='<div style="text-align:center;padding:40px;color:var(--muted);font-size:14px;">ยังไม่มีประวัติ ลองพิมพ์คำถามได้เลยครับ</div>';
    return;
  }
  d.items.forEach(function(item){
    if(item.role==='user') appendUser(item.text);
    else appendBot(item.text,item.sources||[],item.msg_id,item.feedback);
  });
  scrollChat();
}

// ── Chat ─────────────────────────────────────────────────────
function appendUser(text){
  var chat=document.getElementById('chat');
  var div=document.createElement('div');
  div.className='msg user';
  div.innerHTML='<div class="av"><i class="fas fa-user"></i></div>'+
    '<div class="bubble">'+esc(text)+'</div>';
  chat.appendChild(div);
}

function appendBot(text,sources,msgId,fb){
  var chat=document.getElementById('chat');
  var div=document.createElement('div');
  div.className='msg bot';
  var srcHtml=(sources||[]).map(function(s){
    return '<span class="src-tag"><i class="fas fa-database"></i> '+esc(s)+'</span>';
  }).join('');
  var fbHtml=msgId?
    '<div class="fb-row">'+
    '<button class="fb-btn '+(fb===1?'active':'')+'" onclick="feedback('+msgId+',1,this)">👍</button>'+
    '<button class="fb-btn '+(fb===-1?'active':'')+'" onclick="feedback('+msgId+',-1,this)">👎</button>'+
    '</div>':'';
  div.innerHTML='<div class="av"><i class="fas fa-robot"></i></div>'+
    '<div><div class="bubble">'+fmt(text)+'</div>'+
    (srcHtml?'<div class="src-row">'+srcHtml+'</div>':'')+fbHtml+'</div>';
  chat.appendChild(div);
}

function appendLoading(){
  var chat=document.getElementById('chat');
  var div=document.createElement('div');
  div.className='msg bot';div.id='loadingMsg';
  div.innerHTML='<div class="av"><i class="fas fa-robot"></i></div>'+
    '<div class="bubble dots"><span></span><span></span><span></span></div>';
  chat.appendChild(div);scrollChat();return div;
}

async function send(){
  if(!currentThread){toast('เลือกหัวข้อก่อนครับ');return;}
  var el=document.getElementById('q');
  var q=el.value.trim();
  if(!q) return;
  el.value='';
  appendUser(q);scrollChat();
  var loader=appendLoading();
  try{
    var d=await(await fetch('/api/chat',{
      method:'POST',headers:{'Content-Type':'application/json'},
      body:JSON.stringify({question:q,thread_id:currentThread})
    })).json();
    loader.remove();
    appendBot(d.answer,d.sources||[],d.msg_id,0);
    scrollChat();
  }catch(e){
    loader.remove();
    appendBot('เชื่อมต่อไม่ได้ชั่วคราว กรุณาลองใหม่ครับ',[],null,0);
    scrollChat();
  }
}

async function feedback(msgId,val,btn){
  await fetch('/api/feedback',{method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({msg_id:msgId,value:val})});
  btn.closest('.fb-row').querySelectorAll('.fb-btn')
     .forEach(function(b){b.classList.remove('active');});
  btn.classList.add('active');
  toast(val===1?'👍 ขอบคุณ!':'👎 จะนำไปปรับปรุงครับ');
}

function scrollChat(){var c=document.getElementById('chat');c.scrollTop=c.scrollHeight;}

// ── KB Modal ─────────────────────────────────────────────────
function openKBModal(){document.getElementById('kbModal').classList.remove('hide');loadKB();}
function closeKBModal(){document.getElementById('kbModal').classList.add('hide');}
function kbClear(){
  ['kb_id','kb_q','kb_a','kb_t'].forEach(function(id){
    document.getElementById(id).value=id==='kb_id'?'0':'';
  });
}
async function loadKB(){
  var d=await(await fetch('/api/kb/list')).json();
  allKBItems=d.items||[];renderKB(allKBItems);
}
function filterKB(q){
  var f=q.toLowerCase();
  renderKB(allKBItems.filter(function(i){
    return(i.question+i.answer+i.tags).toLowerCase().indexOf(f)>=0;
  }));
}
function renderKB(items){
  document.getElementById('kbCount').textContent=items.length+' รายการ';
  var el=document.getElementById('kbList');
  el.innerHTML='';
  items.forEach(function(item){
    var div=document.createElement('div');
    div.style.cssText='background:var(--bg);border:1px solid var(--line);border-radius:10px;padding:12px;';
    div.innerHTML=
      '<div style="font-weight:700;font-size:13px;margin-bottom:4px;color:var(--text);">#'+item.id+' '+esc(item.question)+'</div>'+
      '<div style="font-size:12px;color:var(--muted);max-height:42px;overflow:hidden;margin-bottom:8px;">'+
        esc(item.answer)+'</div>'+
      '<div style="display:flex;justify-content:space-between;align-items:center;gap:8px;">'+
        '<span style="font-size:11px;color:var(--muted);">'+esc(item.tags||'')+'</span>'+
        '<div style="display:flex;gap:6px;">'+
          '<button class="btn btn2 btn-sm" onclick="kbEdit('+item.id+','+
            JSON.stringify(item.question)+','+JSON.stringify(item.answer)+','+
            JSON.stringify(item.tags||'')+')"><i class="fas fa-edit"></i></button>'+
          '<button class="btn btn-danger btn-sm" onclick="kbDelete('+item.id+')">'+
            '<i class="fas fa-trash"></i></button>'+
        '</div></div>';
    el.appendChild(div);
  });
}
function kbEdit(id,q,a,t){
  document.getElementById('kb_id').value=id;
  document.getElementById('kb_q').value=q;
  document.getElementById('kb_a').value=a;
  document.getElementById('kb_t').value=t;
  document.getElementById('kb_q').focus();
}
async function kbSave(){
  var q=document.getElementById('kb_q').value.trim();
  var a=document.getElementById('kb_a').value.trim();
  if(!q||!a){toast('กรุณากรอกคำถามและคำตอบ');return;}
  await fetch('/api/kb/upsert',{method:'POST',
    headers:{'Content-Type':'application/json'},
    body:JSON.stringify({id:parseInt(document.getElementById('kb_id').value)||null,
      question:q,answer:a,tags:document.getElementById('kb_t').value.trim()})});
  toast('บันทึกแล้ว AI จะเรียนรู้ทันที');
  kbClear();loadKB();
}
async function kbDelete(id){
  if(!confirm('ลบ KB #'+id+' ?')) return;
  await fetch('/api/kb/delete',{method:'POST',
    headers:{'Content-Type':'application/json'},body:JSON.stringify({id:id})});
  toast('ลบ #'+id+' เรียบร้อย');loadKB();
}

// ── Upload Modal (Background Job + Polling) ──────────────────
function openUploadModal(){
  document.getElementById('uploadModal').classList.remove('hide');
  resetUploadUI();
}
function closeUploadModal(){
  cancelUpload();
  document.getElementById('uploadModal').classList.add('hide');
}
function resetUploadUI(){
  if(_pollTimer){clearInterval(_pollTimer);_pollTimer=null;}
  document.getElementById('uploadProgress').classList.add('hide');
  document.getElementById('uploadResult').style.display='none';
  document.getElementById('cancelBtn').classList.add('hide');
  document.getElementById('dropZone').style.display='block';
  document.getElementById('progressBar').style.width='0%';
  document.getElementById('fileInput').value='';
  _uploadCtrl=null;
}
function cancelUpload(){
  if(_uploadCtrl){_uploadCtrl.abort();_uploadCtrl=null;}
  if(_pollTimer){clearInterval(_pollTimer);_pollTimer=null;}
  resetUploadUI();
}
function handleDrop(e){
  e.preventDefault();
  document.getElementById('dropZone').classList.remove('drag');
  var file=e.dataTransfer.files[0];
  if(file) startUpload(file);
}

async function startUpload(file){
  if(!file) return;
  var ext=file.name.split('.').pop().toLowerCase();
  if(['pdf','docx'].indexOf(ext)<0){toast('รองรับเฉพาะ PDF และ DOCX เท่านั้น');return;}
  if(file.size>15*1024*1024){toast('ไฟล์ใหญ่เกิน 15MB');return;}

  document.getElementById('dropZone').style.display='none';
  document.getElementById('uploadProgress').classList.remove('hide');
  document.getElementById('cancelBtn').classList.remove('hide');
  document.getElementById('uploadResult').style.display='none';
  document.getElementById('uploadProgressText').textContent='กำลังอัปโหลด "'+file.name+'"...';
  var bar=document.getElementById('progressBar');
  bar.style.width='5%';

  // Step 1: ส่งไฟล์ รับ job_id ทันที
  var jobId;
  try{
    _uploadCtrl=new AbortController();
    var fd=new FormData();
    fd.append('file',file);
    var resp=await fetch('/api/upload',{method:'POST',body:fd,signal:_uploadCtrl.signal});
    var d=await resp.json();
    if(!d.ok){showUploadError(d.error||'อัปโหลดไม่สำเร็จ');return;}
    jobId=d.job_id;
  }catch(e){
    showUploadError(e.name==='AbortError'?'ยกเลิกการอัปโหลด':e.message);
    return;
  }

  document.getElementById('uploadProgressText').textContent=
    'กำลังประมวลผล PDF... (อาจใช้เวลา 2-3 นาที)';

  // Step 2: Poll status ทุก 2 วิ
  var attempts=0;
  _pollTimer=setInterval(async function(){
    if(++attempts>600){
      clearInterval(_pollTimer);_pollTimer=null;
      showUploadError('ประมวลผลนานเกินไป กรุณาลองใหม่ครับ');
      return;
    }
    try{
      var job=await(await fetch('/api/upload/status/'+jobId)).json();
      bar.style.width=job.progress+'%';
      document.getElementById('uploadProgressText').textContent=
        job.message||'กำลังประมวลผล...';
      if(job.status==='done'){
        clearInterval(_pollTimer);_pollTimer=null;
        showUploadSuccess(job.message);
        loadKB();
      }else if(job.status==='error'){
        clearInterval(_pollTimer);_pollTimer=null;
        showUploadError(job.message);
      }
    }catch(e){
      console.warn('poll:',e.message);
    }
  },2000);
}

function showUploadSuccess(msg){
  document.getElementById('uploadProgress').classList.add('hide');
  document.getElementById('cancelBtn').classList.add('hide');
  var el=document.getElementById('uploadResult');
  el.style.cssText='display:block;background:#ECFDF5;border:1px solid #A7F3D0;'+
    'color:#065F46;border-radius:10px;padding:20px;text-align:center;';
  el.innerHTML='<i class="fas fa-check-circle" style="font-size:32px;margin-bottom:10px;display:block;"></i>'+
    '<b style="font-size:16px;">นำเข้าสำเร็จ!</b>'+
    '<div style="font-size:13px;margin-top:8px;">'+esc(msg)+'</div>'+
    '<button class="btn btn2 btn-sm" style="margin-top:12px;" onclick="resetUploadUI()">'+
    '<i class="fas fa-plus"></i> อัปโหลดไฟล์อื่น</button>';
}

function showUploadError(msg){
  document.getElementById('uploadProgress').classList.add('hide');
  document.getElementById('cancelBtn').classList.add('hide');
  var el=document.getElementById('uploadResult');
  el.style.cssText='display:block;background:#FFF5F5;border:1px solid #FC8181;'+
    'color:#C53030;border-radius:10px;padding:20px;text-align:center;';
  el.innerHTML='<i class="fas fa-times-circle" style="font-size:32px;margin-bottom:10px;display:block;"></i>'+
    '<b>เกิดข้อผิดพลาด</b>'+
    '<div style="font-size:13px;margin-top:8px;">'+esc(msg)+'</div>'+
    '<button class="btn btn2 btn-sm" style="margin-top:12px;" onclick="resetUploadUI()">'+
    '<i class="fas fa-redo"></i> ลองใหม่</button>';
}

// ── Helpers ──────────────────────────────────────────────────
function esc(s){
  return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;')
    .replace(/>/g,'&gt;').replace(/"/g,'&quot;');
}
function fmt(text){
  return esc(text).replace(/\\n/g,'<br/>')
    .replace(/\\*\\*(.*?)\\*\\*/g,'<b>$1</b>')
    .replace(/`(.*?)`/g,'<code style="background:var(--bg);padding:1px 5px;border-radius:4px;font-size:13px;">$1</code>');
}
function toast(msg){
  var el=document.createElement('div');
  el.className='toast';el.textContent=msg;
  document.body.appendChild(el);
  setTimeout(function(){el.remove();},3200);
}
window.onload=loadThreads;
</script>
"""
    return _shell("Chat", body)
