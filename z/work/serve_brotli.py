from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


class BrotliHandler(SimpleHTTPRequestHandler):
    extensions_map = {
        **SimpleHTTPRequestHandler.extensions_map,
        ".br": "application/octet-stream",
        ".wasm": "application/wasm",
    }

    def end_headers(self):
        if self.path.split("?", 1)[0].endswith(".br"):
            self.send_header("Content-Encoding", "br")
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def guess_type(self, path):
        if path.endswith(".wasm.br"):
            return "application/wasm"
        if path.endswith(".js.br"):
            return "application/javascript"
        return super().guess_type(path)


if __name__ == "__main__":
    root = Path("/Users/a1-6/Desktop/a2/Fireflystorybook/Builds/WebGL")
    handler = lambda *args, **kwargs: BrotliHandler(*args, directory=str(root), **kwargs)
    ThreadingHTTPServer(("127.0.0.1", 8125), handler).serve_forever()
