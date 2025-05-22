import webview
import os

class App:
    def __init__(self, title="My App", html_file=None, js_api=None, width=800, height=600, resizable=True, debug=False):
        self.title = title
        self.html_file_path = self._get_html_path(html_file)
        self.js_api = js_api
        self.width = width
        self.height = height
        self.resizable = resizable
        self.debug = debug
        self.window = None

    def _get_html_path(self, file_name):
        if not file_name:
            return None
        # Assuming html_file is a relative path from the perspective of the calling script
        # For examples, this would typically be os.path.join(os.path.dirname(sys.argv[0]), file_name)
        # For now, let's assume it's made absolute by the caller, or it's a file:// URL
        if os.path.exists(file_name):
             return f'file://{os.path.abspath(file_name)}'
        return file_name # Assume it's already a URL if not a local file

    def _create_window(self):
        self.window = webview.create_window(
            self.title,
            self.html_file_path,
            js_api=self.js_api,
            width=self.width,
            height=self.height,
            resizable=self.resizable
        )

    def run(self, func=None, func_args=()):
        self._create_window()
        webview.start(func, func_args, debug=self.debug)
