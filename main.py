def main():
    bills = [200, 100, 75, 25, 1]
    input_string = input("Gewünschter Betrag > ")
    amount = int(input_string)
    index = 0
    while amount > 0:
        if bills[index] > amount:
            index += 1
        else:
            print(str(bills[index]) + ' KD')
            amount = amount - bills[index]


if __name__ == '__main__':
    main()
