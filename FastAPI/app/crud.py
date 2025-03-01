from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import update
from . import schema, models
from sqlalchemy.sql import text


def save_device_info(db: Session, info: schema.DeviceInfo):
    device_info_model = models.DeviceInfo(**info.dict())
    db.add(device_info_model)
    db.commit()
    db.refresh(device_info_model)
    return device_info_model

def get_device_info(db: Session, token: str = None):
    if token is None:
        return db.query(models.DeviceInfo).all()
    else:
        return db.query(models.DeviceInfo).filter(models.DeviceInfo.token == token).first()

def save_nudges_configuration(db: Session, config: schema.Configuration):
    config_model = models.Configuration(**config.dict())
    db.add(config_model)
    db.commit()
    db.refresh(config_model)
    return config_model

def get_nudges_configuration(db: Session):
    return db.query(models.Configuration).first()

def delete_nudges_configuration(db: Session):
    db.query(models.Configuration).delete()

def error_message(message):
    return {
        'error': message
    }

def update_device_info(db: Session, info: schema.DeviceInfo):
    db.query(models.DeviceInfo).filter(models.DeviceInfo.token == info.token).update({"username": (info.username)})    
    return db.commit()
