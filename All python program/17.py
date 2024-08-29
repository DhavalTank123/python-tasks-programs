'''Write a program a function for ATM machine which takes amount as input and output should be number of notes of each
denomination. The ATM has notes in following denomination : 2000, 500, 100.'''

def atm_machine(amount):
    denominations = [2000, 500, 100]
    notes = [0, 0, 0]

    for i in range(len(denominations)):
        if amount >= denominations[i]:
            notes[i] = amount // denominations[i]
            amount %= denominations[i]

    return notes

if __name__ == '__main__':

    amount = int(input("Enter the amount: "))
    notes = atm_machine(amount)
    print("Number of 2000 rupee notes:", notes[0])
    print("Number of 500 rupee notes:", notes[1])
    print("Number of 100 rupee notes:", notes[2])
