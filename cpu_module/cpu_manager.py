class PCManager:
    # Attributes
    psutil_ = __import__("psutil")
    # Methods
    def __init__(self):
        print("Starting the PC analysis...")
    def print_cpu_usage(self, seconds:int)->str:
        """
        Prints the CPU percentage used in x amount of seconds
        """
        try:
            # Calling psutil.cpu_precent() for x seconds
            return 'The CPU usage is: {}%, in {} seconds of analysis.'.format(self.psutil_.cpu_percent(seconds), seconds)
        except Exception as error:
            return "ERROR: {}".format(error)
    def print_ram_performance(self)->str:
        """
        """
    def __del__(self):
        print("Finished the PC analysis...")