import random

SUIT_TUPLE = ("Spades", "Hearts", "Clubs", "Diamonds")
RANK_TUPLE = ("Ace", "2", "3", "4", "5", "6", "7", "8", "9", "Jack", "Queen", "King")

NCARDS = 8

# This function will take a deck annd return a random card
def getCard(deckListIn):
    thisCard = deckListIn.pop()  # pop a card off the top of the deck and return it
    return thisCard


# pass in a deck and this function will shuffle and then return it
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()  # Make a copy of the starting deck
    random.shuffle(deckListOut)
    return deckListOut


# main program
print("Welcome to Higher or Lower")
print(
    "You have to choose whether the next card to be shown will be higher or lower than the current card."
)
print("Getting it right adds 20 points; get it wrong and you lose 15 points.")
print("You have 50 points to start.")
print()

startingDeckList = []
for suit in SUIT_TUPLE:
    for thisValue, rank in enumerate(RANK_TUPLE):
        cardDict = {"rank": rank, "suit": suit, "value": thisValue + 1}
        startingDeckList.append(cardDict)

score = 50

while True:  # play multiple games
    print()
    gameDeckList = shuffle(startingDeckList)
    currentCardDict = getCard(gameDeckList)
    currentCardRank = currentCardDict["rank"]
    currentCardValue = currentCardDict["value"]
    currentCardSuit = currentCardDict["suit"]
    print("Starting card is: ", currentCardRank + " of " + currentCardSuit)
    print()

    for cardNumber in range(0, NCARDS):  # play 1 game of this many cards
        answer = input(
            "Will the next card be higher or lower than the "
            + currentCardRank
            + " of "
            + currentCardSuit
            + "?  (enter h or l): "
        )
        answer = answer.casefold()  # force lowercase
        nextCardDict = getCard(gameDeckList)
        nextCardRank = nextCardDict["rank"]
        nextCardSuit = nextCardDict["suit"]
        nextCardValue = nextCardDict["value"]
        print("Next card is: ", nextCardRank + " of " + nextCardSuit)

        if answer == "h":
            if nextCardValue > currentCardValue:
                print("You got it right, it was higher")
                score = score + 20
            else:
                print("Sorry, it was not higher")
                score = score - 15
        elif answer == "l":
            if nextCardValue < currentCardValue:
                print("You got it right, it was lower")
                score = score + 20
            else:
                print("Sorry, it was not lower")
                score = score - 15

        print("Your score is: ", score)
        print()
        currentCardRank = nextCardRank
        currentCardValue = nextCardValue  # don't need to update the suit

    goAgain = input('To play again, press ENTER, or "q" to quit: ')
    goAgain = goAgain.casefold()
    if goAgain == "q":
        break

print("OK bye")
