import logging
import sys

taskName = sys.argv[0].replace('.py','')

logging.basicConfig(
    filename='automacao.log',
    level=logging.DEBUG,
    format='%(asctime)s - '+taskName+' - %(levelname)s: %(message)s',
    datefmt = '%d-%m-%Y %H:%M:%S',
    encoding='utf-8',
)

logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
logging.error('And non-ASCII stuff, too, like Øresund and Malmö')
logging.critical('critical message')

logging.info("Robô iniciado")
try:
    # tarefa
    logging.info("Tarefa concluída com sucesso")
except Exception as e:
    logging.error(f"Erro durante a execução: {e}")
