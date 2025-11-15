import sys
import webbrowser
import tempfile

def main():
    print("=== AI Lab HTML Viewer ===")
    print("HTML 코드를 입력하세요.")
    print("입력이 끝나면 Ctrl+Z (Windows) 또는 Ctrl+D (Mac/Linux)를 누르세요:\n")

    html_lines = []
    try:
        while True:
            line = input()
            html_lines.append(line)
    except EOFError:
        pass

    html_code = "\n".join(html_lines)

    # 임시 HTML 파일로 저장 후 브라우저 열기
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".html") as f:
        f.write(html_code)
        print(f"\n[완료] 브라우저에서 열기: {f.name}")
        webbrowser.open(f.name)

