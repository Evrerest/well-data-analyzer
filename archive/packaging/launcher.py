from __future__ import annotations

import os
import sys
from pathlib import Path

from streamlit.web import bootstrap


def project_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)
    return Path(__file__).resolve().parent


def main() -> None:
    root = project_root()
    app_path = root / "app.py"

    os.environ.setdefault("STREAMLIT_BROWSER_GATHER_USAGE_STATS", "false")
    os.environ.setdefault("STREAMLIT_SERVER_HEADLESS", "false")
    os.environ.setdefault("STREAMLIT_SERVER_FILE_WATCHER_TYPE", "none")

    sys.argv = [
        "streamlit",
        "run",
        str(app_path),
        "--server.headless=false",
        "--server.fileWatcherType=none",
    ]
    bootstrap.run(str(app_path), False, [], {})


if __name__ == "__main__":
    main()
