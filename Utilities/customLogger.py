import logging

class LogGen:
    @staticmethod
    def loggen():
        # logging.basicConfig(filename="C:/Users/Admin/PycharmProjects/Hybrid_framework/Logs/Logs.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s:', datefmt='%m/%d/%Y %I:%M:%S %p')

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        f = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s:')
        fh = logging.FileHandler('.\\Logs\\automation.log')
        fh.setFormatter(f)
        logger.addHandler(fh)
        return logger
