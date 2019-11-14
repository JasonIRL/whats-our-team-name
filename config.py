import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    """Flask Config"""

    SECRET_KEY = os.getenv("SECRET_KEY") or "i-dont-fucking-care"
    SQLALCHEMY_DATABASE_URI = (
        os.getenv("DATABASE_URL") or f"sqlite:///{os.path.join(basedir, 'name.db')}"
    )
