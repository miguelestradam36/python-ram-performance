class PCManager:
    # Attributes
    psutil_ = __import__("psutil")
    os_ = __import__("os")
    # Methods
    def __init__(self):
        print("Starting the PC analysis...")

    def return_cpu_usage(self, seconds:int)->str:
        """
        Returns the CPU percentage used in x amount of seconds
        """
        try:
            # Calling psutil.cpu_precent() for x seconds
            return 'The CPU usage is: {}%, in {} seconds of analysis.'.format(self.psutil_.cpu_percent(seconds), seconds)
        except Exception as error:
            return "ERROR: {}".format(error)
        
    def return_cpu_count(self):
        """
        Returns the number of cores in system
        """
        try:
            return "Number of cores in the system: {}".format(self.os_.cpu_count())
        except Exception as error:
            return "ERROR: {}".format(error)
        
    def return_ram_process_usage(self)->str:
        """
        Returns the RAM memory percentage used by the computer
        """
        try:
            return "This execution has used a total of: {} MB".format(str(round(self.psutil_.Process().memory_info().rss / (1024 * 1024), 2)))
        except Exception as error:
            return "ERROR: {}".format(error)

    
    def return_virtual_memory_usage(self)->str:
        """
        Returns the virtual memory used by the computer
        """
        memory = "Virtual memory used by the computer: {}%".format(round(self.psutil_.virtual_memory().total / (1024.0 ** 3), 2))
        return memory
    
    def __del__(self):
        print("Finished the PC analysis...")