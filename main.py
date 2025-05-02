from extract import extract
from utils.settings import SETTINGS

if __name__ == "__main__":
    extract(SETTINGS.API_URL, SETTINGS.PARAMS)