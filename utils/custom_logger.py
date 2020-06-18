import logging


class CustomLogger:

    def __init__(self):
        fmtStr = "%(asctime)s: %(levelname)s: %(funcName)s Line:%(lineno)d %(message)s"
        dateStr = "%m/%d/%Y %I:%M:%S %p"
        logging.basicConfig(level=logging.DEBUG,
                        filename="output.log",
                        filemode='w',
                        format=fmtStr,
                        datefmt=dateStr)
