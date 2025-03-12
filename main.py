from cpu_module.cpu_manager import PCManager

if __name__ == "__main__":
    object_ = PCManager()
    # CPU percentage usage in 10 seconds
    print(object_.return_cpu_usage(seconds=10))
    # Virtual memory
    print(object_.return_virtual_memory_usage())
    # Cores in the system
    print(object_.return_cpu_count())
    # RAM usage analysis on the PC (RAM used in this process/execution)
    print(object_.return_ram_process_usage())