from cpu_module.cpu_manager import PCManager

if __name__ == "__main__":
    object_ = PCManager()
    # CPU percentage usage in 10 seconds
    print(object_.print_cpu_usage(seconds=10))
    # RAM usage analysis on the PC
    for element in object_.return_ram_performance():
        print(element)
    # Virtual memory
    print(object_.return_virtual_memory_usage())