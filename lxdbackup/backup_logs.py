import logging


class Log:
    def __init__(self) -> None:
        self._setup()
        pass

    def _setup(self):
        self.logger = logging.getLogger()

    def log(self, out, err):
        self.logger.info(out)
        self.logger.error(err)


"""
proc = subprocess.Popen(["cat", "/etc/services"], stdout=subprocess.PIPE, shell=True)
(out, err) = proc.communicate()
logger.INFO("This is the main script. Here's the program output:")
logger.INFO(out)
"""
