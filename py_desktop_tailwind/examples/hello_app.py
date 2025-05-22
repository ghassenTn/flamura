import os
import time
# Adjust import path assuming 'src' is in PYTHONPATH or using a proper install
# For direct execution from repo root, this might require sys.path manipulation
# or running as 'python -m examples.hello_app' if src is structured correctly

# To make the import work when running directly from the examples folder or project root:
import sys
# Get the absolute path to the project root directory (assuming examples is one level down from root)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# Get the absolute path to the src directory
src_path = os.path.join(project_root, 'src')
# Add src to Python path if it's not already there
if src_path not in sys.path:
    sys.path.insert(0, src_path)

from py_desktop_tailwind.core import App 

# Define the API class to expose to JavaScript
class Api:
    def greet_python(self, message):
        print(f"JavaScript says: {message}")
        response_message = "Hi JavaScript, Python here! 👋 Thanks for the message."
        return response_message

def get_example_html_path(file_name):
    # Path relative to this example script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, file_name)

if __name__ == '__main__':
    html_file = get_example_html_path('hello.html')
    api_instance = Api()

    # Create the app instance using the library's App class
    my_app = App(
        title="My Library App",
        html_file=html_file,
        js_api=api_instance,
        debug=True
    )

    # Define the function to be called after webview starts (for Python-to-JS call)
    # This function now needs to access my_app.window
    def call_js_after_load():
        try:
            time.sleep(1) 
            new_message = "Message updated by Python via Library App!"
            if my_app.window: # Check if window object exists
                my_app.window.evaluate_js(f'updateMessage("{new_message}")')
                print(f"Called JS to update message to: '{new_message}'")
            else:
                print("Error: App window not initialized for JS call.")
        except Exception as e:
            print(f"Error calling JavaScript: {e}")

    my_app.run(func=call_js_after_load)
