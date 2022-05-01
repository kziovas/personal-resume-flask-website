import os
from resume_app import ResumeApp
from injector import Injector
from core import CoreModule


def create_app():
    injector = Injector(modules=[CoreModule])
    resume_app = injector.get(ResumeApp)
    app = resume_app.configure_app()
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = False

    # app.run(
    #     host=resume_app.config_service.host, port=resume_app.config_service.app_port
    # )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run()
