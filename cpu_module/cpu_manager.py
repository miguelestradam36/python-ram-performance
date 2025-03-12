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
        
    def return_ram_usage(self)->list:
        """
        Returns the RAM memory percentage used by the computer
        """
        analysis_information = []
        # Getting all memory using os.popen()
        total_memory, used_memory, free_memory = map(int, self.os_.popen('free -t -m').readlines()[-1].split()[1:])
        # Memory usage
        object_1 = str("Percentage used in the RAM memory of the PC: {}".format(round((used_memory/total_memory) * 100, 2)))
        # Free memory
        object_2 = str("Percentage of free RAM memory on the PC: {}".format(round((free_memory) * 100, 2)))
        analysis_information.append(object_1)
        analysis_information.append(object_2)
        return analysis_information
    
    def return_virtual_memory_usage(self)->str:
        """
        Returns the virtual memory used by the computer
        """
        memory = "Virtual memory used by the computer: {}".format(self.psutil_.virtual_memory().total / (1024.0 ** 3))
        return memory
    def __del__(self):
        print("Finished the PC analysis...")