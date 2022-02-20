from pocket_api import *
import pudb

pu.db

retrieve_json = retrieve(detailType='complete', sort='newest', search='sei', domain='')
model(retrieve_json)
pocket = Pocket(**retrieve_json)