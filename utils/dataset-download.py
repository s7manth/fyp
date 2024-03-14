from huggingface_hub import hf_hub_download
import pandas as pd

REPO_ID = "YOUR_REPO_ID"
FILENAME = "data.csv"

dataset = pd.read_csv(
    hf_hub_download(repo_id=REPO_ID, filename=FILENAME, repo_type="dataset")
)
