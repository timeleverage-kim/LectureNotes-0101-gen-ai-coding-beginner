#!/usr/bin/env python3
"""src/*.md 의 {{code: 경로}} 를 실제 코드 파일 내용으로 바꿔 md/ 에 저장한다."""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANG = {".html": "html", ".css": "css", ".js": "javascript", ".py": "python", ".svg": "xml", ".txt": "text"}

def expand(m):
    rel = m.group(1).strip()
    path = ROOT / "code" / rel
    if not path.exists():
        sys.exit(f"[build] 코드 파일이 없습니다: {rel}")
    text = path.read_text(encoding="utf-8").rstrip("\n")
    return f"```{LANG.get(path.suffix, '')}\n{text}\n```"

def main():
    out = ROOT / "md"
    out.mkdir(exist_ok=True)
    for src in sorted((ROOT / "src").glob("*.md")):
        body = re.sub(r"\{\{code:\s*([^}]+)\}\}", expand, src.read_text(encoding="utf-8"))
        (out / src.name).write_text(body, encoding="utf-8")
        print("built", src.name)

main()
