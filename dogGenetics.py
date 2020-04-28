import random
def main():
    resultsAdded = 0
    name = input("What is your dog's name? ")
    print(f"Well then, I have this highly reliable report on {name}'s prestigious background right here.\n")
    print(f"{name} is: \n")
    genResults = genetics()
    
    if genResults[0] != 0:
        print(f"{genResults[0]}% Pitbull")
    if genResults[1] != 0:
        print(f"{genResults[1]}% Chihuhua")
    if genResults[2] != 0:
        print(f"{genResults[2]}% St. Bernard")
    if genResults[3] != 0:
        print(f"{genResults[3]}% Golden Retriever")
    for x in genResults:
        resultsAdded += x
    if resultsAdded < 100:
        resultsAdded = 100 - resultsAdded
        print(f"{resultsAdded}% Pug")
        
    print("\nWow, that's QUITE the dog!")
def genetics():
    peak = 101
    rGen = random.randrange(1, peak, 1)
    genArray = []
    for i in range(4):
        genArray.append(rGen)
        peak -= rGen
        if peak > 1:
            rGen = random.randrange(0, peak, 1)
        else:
            rGen = 0
            
    return genArray
    
if __name__ == "__main__":
    main()