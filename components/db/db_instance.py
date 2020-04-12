from components.db.connection import *
from models.db_models import *
from components.config.logsmanager import logger


def create_tables():
    db.create_tables([Usuario, Reserva, Persona, Dispositivo])
    logger.info("TABLES OK")


def connect_db():
    db.connect(db.connect(reuse_if_open=True))
    create_tables()
    logger.info("db connected")
