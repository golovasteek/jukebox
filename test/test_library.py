from tempfile import TemporaryDirectory
from jukebox.__main__ import load_library
from pathlib import Path

def test_parse():
    with TemporaryDirectory() as d:
        with open(Path(d) / "config.json", "w+") as f:
            f.write("""{"1": "/some/path"}""")
        
        config = load_library(Path(d))
        assert 1 in config
        assert config[1] == "/some/path"
