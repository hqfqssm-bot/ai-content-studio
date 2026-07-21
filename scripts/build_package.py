import os, shutil, zipfile
from pathlib import Path

ROOT = Path(r'C:\Users\41896\Documents\11\ai-content-studio')
OUT = ROOT.parent / 'ai-content-studio-sellable'
BUILD = OUT / 'ai-content-studio-v1.0'
ZIP_PATH = ROOT.parent / 'ai-content-studio-v1.0.zip'

if BUILD.exists():
    shutil.rmtree(BUILD)
OUT.mkdir(parents=True, exist_ok=True)

INCLUDE = [
    'backend/app/',
    'backend/requirements.txt',
    'backend/.env.example',
    'frontend/index.html',
    'docker-compose.yml',
    'Dockerfile',
    'nginx.conf',
    'start.bat',
    'README.md',
]

for path in INCLUDE:
    src = ROOT / path
    dst = BUILD / path
    if src.is_dir():
        shutil.copytree(src, dst, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    elif src.exists():
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

env_content = "SECRET_KEY=replace-with-a-secure-random-key-in-production\nDATABASE_URL=sqlite:///./app.db\nOPENAI_API_KEY=\nOPENAI_BASE_URL=https://api.openai.com/v1\nDEFAULT_MODEL=gpt-4o-mini\nSTRIPE_SECRET_KEY=\nSTRIPE_PUBLISHABLE_KEY=\nSTRIPE_WEBHOOK_SECRET=\nFRONTEND_URL=http://localhost:8000\n"
(BUILD / '.env').write_text(env_content)

install_md = "# AI Content Studio - Installation Guide\n\n## Quick Start (Local)\n1. Install Python 3.10+\n2. Run: cd backend && pip install -r requirements.txt\n3. Copy .env.example to .env and fill in your keys\n4. Run: cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload\n5. Open http://localhost:8000\n\n## Docker (Production)\n1. Set your environment variables in .env\n2. Run: docker compose up -d\n3. Open http://localhost\n\n## Required Keys\n- OPENAI_API_KEY: For AI content generation\n- STRIPE_SECRET_KEY: (Optional) For Pro subscription payments\n"
(BUILD / 'INSTALL.md').write_text(install_md)

if ZIP_PATH.exists():
    ZIP_PATH.unlink()
with zipfile.ZipFile(ZIP_PATH, 'w', zipfile.ZIP_DEFLATED) as zf:
    for f in BUILD.rglob('*'):
        if f.is_file():
            arcname = f.relative_to(BUILD.parent)
            zf.write(f, arcname)

print("Package created at: " + str(ZIP_PATH))
print("Size: " + str(os.path.getsize(ZIP_PATH) / 1024) + " KB")
