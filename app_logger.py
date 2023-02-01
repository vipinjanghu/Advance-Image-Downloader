import logging
def log():
    logging.basicConfig(filename='app.log', level=logging.INFO,format='%(asctime)s  %(name)s  %(levelname)s: %(message)s')
    return logging.getLogger(__name__)
