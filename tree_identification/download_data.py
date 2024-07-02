import zipfile
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi
from loguru import logger


def authenticate_kaggle() -> KaggleApi:
    logger.info("Authenticating Kaggle API")
    api = KaggleApi()
    api.authenticate()
    return api
    
    
def download_data(kaggle_dataset_url:str, save_path:Path = Path("data")) -> None:
    dataset_name = Path(kaggle_dataset_url).stem
    logger.info(f"Downloading {dataset_name} from Kaggle")
    api = authenticate_kaggle()
    api.dataset_download_files(kaggle_dataset_url, path = save_path)
    return None


def unzip_data(save_path:Path = Path("data")) -> None:
    logger.info("Unzipping data")
    zip_file_path = list(save_path.glob("*.zip"))[0]
    extract_dir = Path(save_path, zip_file_path.stem)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    return None


def main() -> None:
    kaggle_dataset_url = "erickendric/tree-dataset-of-urban-street-classification-tree"
    download_data(kaggle_dataset_url = kaggle_dataset_url)
    unzip_data()
    return None

if __name__ == "__main__":
    main()