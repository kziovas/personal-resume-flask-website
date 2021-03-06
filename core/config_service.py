import os
import json
from pathlib import Path
from injector import singleton, inject
from shared import (
    LOG_LEVEL,
    CONFIG_FOLDER_NAME,
    CONFIG_FILE_NAME,
    FLASK_SETTINGS_FILE_NAME,
)


@singleton
class ConfigService:
    def __init__(self) -> None:
        self.config_filepath: str = None
        self.flask_settings_filepath: str = None
        self.safe_key: str = None
        self.log_level: str = None
        self.host: str = None
        self.app_port: int = None
        self.config_folder_path: str = None
        self.config_folder_name: str = None

    def load(self):

        self.config_folder_path = (
            Path(__file__).parents[1].absolute().joinpath(CONFIG_FOLDER_NAME)
        )

        self.flask_settings_filepath = self.config_folder_path.joinpath(
            FLASK_SETTINGS_FILE_NAME
        )

        self.config_filepath = self.config_folder_path.joinpath(CONFIG_FILE_NAME)

        with open(self.config_filepath, "r") as config_file:
            config_data = json.load(config_file)

            self.log_level = config_data[LOG_LEVEL]
            self.host = config_data["HOST"]
            self.app_port = int(config_data["APP_PORT"])
            del config_data
