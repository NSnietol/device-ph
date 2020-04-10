import subprocess

from config import logsmanager as log


class DataBaseUp():

    def __init__(self, *args, **kwargs):
        pass

    def init(self):
        try:
            log.logger.info('Iniciando  db')
            subprocess.call(['docker-compose','-f','db/docker-compose.yml','up','-d'])

        except Exception as e1:
            log.logger.error('No se pudo iniciar la db'+str(e1))
            raise e1
        





