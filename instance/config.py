class Config(object):
    SECRET_KEY = 'hjshjhdjah kjshkjdhjs'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dt_admin:dt2016@localhost/dreamteam_db'
    DEBUG = True


class DevelopmentConfig(Config):
    SECRET_KEY = 'hjshjhdjah kjshkjdhjs'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dt_admin:dt2016@localhost/dreamteam_db'
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    SECRET_KEY = 'hjshjhdjah kjshkjdhjs'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dt_admin:dt2016@localhost/dreamteam_db'
    DEBUG = False


class TestingConfig(Config):
    SECRET_KEY = 'hjshjhdjah kjshkjdhjs'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dt_admin:dt2016@localhost/dreamteam_db'
    TESTING = True

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
