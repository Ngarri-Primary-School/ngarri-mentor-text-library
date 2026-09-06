"""Build current text-checked fixture; earlier builders remain preserved."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name("full_text_examples.py")), run_name="__main__")
