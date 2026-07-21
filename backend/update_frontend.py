content = open(r'C:\Users\41896\Documents\11\ai-content-studio\frontend\index.html', encoding='utf-8').read()

old_sb = 'id="sidebarName" style="font-weight:600;color:var(--text-sidebar-active)">User</div>'
new_sb = 'id="sidebarName" style="font-weight:600;color:var(--text-sidebar-active)">User</div><span id="proBadge" style="display:none;background:#6366f1;color:#fff;font-size:.6rem;font-weight:700;padding:1px 6px;border-radius:4px;margin-left:4px;vertical-align:middle;letter-spacing:.5px">PRO</span>'
content = content.replace(old_sb, new_sb, 1)

old_ui = 'CURRENT_USER = user;'
new_ui = 'CURRENT_USER = user;\n    var pb = document.getElementById("proBadge");\n    if (pb) pb.style.display = user.is_pro ? "inline" : "none";'
content = content.replace(old_ui, new_ui, 1)

old_init = 'if (TOKEN) {\n  showApp();\n  loadDashboard();\n  loadContentTypes();\n  updateUserInfo();\n} else {\n  showAuth();\n}'
new_init = 'var params = new URLSearchParams(window.location.search);\nif (params.get("payment") === "success") {\n  toast("Payment successful! Welcome to Pro!", "success");\n  window.history.replaceState({}, "", window.location.pathname);\n}\nif (TOKEN) {\n  showApp();\n  loadDashboard();\n  loadContentTypes();\n  updateUserInfo();\n} else {\n  showAuth();\n}'
content = content.replace(old_init, new_init, 1)

open(r'C:\Users\41896\Documents\11\ai-content-studio\frontend\index.html', 'w', encoding='utf-8').write(content)
print('Frontend updated')
