from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PAGE_PATH = Path(__file__).resolve().parent / "public" / "index.html"


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path not in ("/", "/index.html"):
            self.send_error(404)
            return

        content = PAGE_PATH.read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.end_headers()
        self.wfile.write(content)


if __name__ == "__main__":
    address = ("127.0.0.1", 8000)
    print(f"サイトを起動しました: http://{address[0]}:{address[1]}")
    try:
        ThreadingHTTPServer(address, Handler).serve_forever()
    except KeyboardInterrupt:
        print("\nサイトを終了しました。")
