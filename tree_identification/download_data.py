"""
Kaggle Dataset Downloader and Extractor

This module provides functionality to authenticate with the Kaggle API, download a dataset,
and unzip the downloaded dataset files. It utilizes the `loguru` library for logging and
the `kaggle` library for API interactions.

Functions:
    authenticate_kaggle() -> KaggleApi:
        Authenticates the Kaggle API using the kaggle library.

    download_data(kaggle_dataset_url: str, save_path: Path = Path("tree_identification", "data")) -> None:
        Downloads a dataset from Kaggle to the specified path.

    unzip_data(save_path: Path = Path("tree_identification", "data"), delete_after: bool = False) -> None:
        Unzips the downloaded dataset files and optionally deletes the original zip files.

    main() -> None:
        Main function to download and unzip the dataset.
"""

import zipfile
from pathlib import Path

from kaggle.api.kaggle_api_extended import KaggleApi
from loguru import logger


def authenticate_kaggle() -> KaggleApi:
    """
    Authenticates the Kaggle API using the Kaggle library.
    
    Returns:
        KaggleApi: An authenticated Kaggle API object.
    """
    logger.info("Authenticating Kaggle API")
    api = KaggleApi()
    api.authenticate()
    return api

def download_data(kaggle_dataset_url: str, save_path: Path = Path("tree_identification", "data")) -> None:
    """
    Downloads a dataset from Kaggle to the specified path.
    
    Args:
        kaggle_dataset_url (str): The URL of the Kaggle dataset to download.
        save_path (Path, optional): The path where the dataset will be saved. Defaults to Path("tree_identification", "data").
    
    Returns:
        None
    """
    dataset_name = Path(kaggle_dataset_url).stem
    logger.info(f"Downloading {dataset_name} from Kaggle")
    api = authenticate_kaggle()
    api.dataset_download_files(kaggle_dataset_url, path=save_path, quiet=False)
    return None

def unzip_data(save_path: Path = Path("tree_identification", "data"), delete_after: bool = False) -> None:
    """
    Unzips the downloaded dataset files and optionally deletes the original zip files.
    
    Args:
        save_path (Path, optional): The path where the zip files are located. Defaults to Path("tree_identification", "data").
        delete_after (bool, optional): Whether to delete the zip files after extraction. Defaults to False.
    
    Returns:
        None
    """
    logger.info("Unzipping data")
    zip_file_path = list(save_path.glob("*.zip"))[0]
    extract_dir = Path(save_path, zip_file_path.stem)
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    if delete_after:
        logger.debug("Deleting original .zip file")
        zip_file_path.unlink()
    return None

def main() -> None:
    """
    Main function to download and unzip the dataset.
    
    Returns:
        None
    """
    kaggle_dataset_url = "erickendric/tree-dataset-of-urban-street-classification-tree"
    download_data(kaggle_dataset_url=kaggle_dataset_url)
    unzip_data(delete_after=True)
    return None

if __name__ == "__main__":
    main()
if __name__ == "__main__":
    main()
