import os
import redis
from app import app
import logging

def get_pictures(path=None, pics=[]):
    logging.debug('yooo {} ... {}'.format(path, pics))

    pics=[]
    if path != '.' and path != '/':
        files = [f for f in os.listdir(app.static_folder + '/images/' + path) ]
        for f in files:
            pics.append(f)
    return pics

