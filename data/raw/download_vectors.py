"""
Download Hamilton et al. (2016) HistWords pre-trained vectors.
English Google Books, decade embeddings 1800s-1990s.
Run: pixi run download
"""

import os
import urllib.request
import zipfile
from pathlib import Path

RAW = Path(__file__).parent
BASE_URL = "https://nlp.stanford.edu/data/histwords"

# English Google Books decade vectors
DECADES = list(range(1800, 2000, 10))
FILES = [f"eng-all_sgns/{d}-w.npy" for d in DECADES] + \
        [f"eng-all_sgns/{d}-vocab.pkl" for d in DECADES]

def download_histwords():
    target = RAW / "eng-all_sgns"
    target.mkdir(exist_ok=True)

    zip_url = f"{BASE_URL}/eng-all_sgns.zip"
    zip_path = RAW / "eng-all_sgns.zip"

    if not zip_path.exists():
        print(f"Downloading {zip_url} (~1.5 GB)...")
        urllib.request.urlretrieve(zip_url, zip_path,
            reporthook=lambda b, bs, t: print(f"  {b*bs/1e6:.0f}/{t/1e6:.0f} MB", end="\r"))
        print()

    print("Extracting...")
    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(RAW)
    print(f"Done. Vectors in {target}")

if __name__ == "__main__":
    download_histwords()
