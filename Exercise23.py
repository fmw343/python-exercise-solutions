with open('happynumbers.txt', 'r') as happy:
    with open('primenumbers.txt', 'r') as prime:
        list1 = [int(number.strip()) for number in happy]
        list2 = [int(number.strip()) for number in prime]

        print([number for number in list1 if number in list2])
