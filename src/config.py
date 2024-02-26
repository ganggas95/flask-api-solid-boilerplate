from envs import DATABASE_URL, ENV


class BaseConfig:
    ENV = "development"
    FLASK_ENV = "development"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL


class DevelopmentConfig(BaseConfig):
    ENV = "development"
    FLASK_ENV = "development"
    TESTING = False
    DEBUG = True


class TestingConfig(BaseConfig):
    ENV = "testing"
    FLASK_ENV = "testing"
    TESTING = True
    DEBUG = False


class ProductionConfig(BaseConfig):
    ENV = "production"
    FLASK_ENV = "production"
    TESTING = False
    DEBUG = False


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}


def get_config() -> BaseConfig:
    return config[ENV]
