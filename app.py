import os
import sys

# Configure the src folder as a root folder
# So when we import the factory, we can import with src as a root
current_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(1, os.path.join(current_dir, "src"))

from factory import APP as app  # noqa;

if __name__ == "__main__":
    app.run("0.0.0.0", 8080, debug=True, load_dotenv=True, use_reloader=True)
