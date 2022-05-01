import json
from flask import Flask
from logging import Logger
from injector import inject, singleton
from core import ConfigService
from views import home_bp, about_bp
from shared import APP_NAME


@singleton
class ResumeApp:
    @inject
    def __init__(
        self,
        logger: Logger,
        config_service: ConfigService,
    ) -> None:
        self.logger = logger
        self.config_service = config_service

    def configure_app(self, name: str = APP_NAME):
        app = Flask(name)
        try:
            self.config_service.load()
        except Exception as exc:
            self.logger.error(f"Loading configuration file failed due to: {exc}")
            raise exc

        # Load app settings
        with open(self.config_service.flask_settings_filepath) as f:
            settings = json.load(f)

        app.config.update(settings)

        # Initiliaze configuration and URL rules for all views

        # Register blueprints
        app.register_blueprint(home_bp)
        app.register_blueprint(about_bp)

        return app
