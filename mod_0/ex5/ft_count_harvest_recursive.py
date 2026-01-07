def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def counter(current):
        if current > n:
            return
        print("Day", current)
        counter(current + 1)

    counter(1)
    print("Harvest time!")
