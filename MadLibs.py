#02/15/2021, Mad Libs Random Stroy Generator

name = input("what is your name?")
print(name)

exclamation = input("Enter an exclamation word:")
adverb = input ("Enter an adverb:")
noun = input("Enter a noun:")
adjective = input("Enter an adjective:")
nounTwo = input("Enter a noun:")


#our story
# f-strings have the f prefix and use {} brackets to evaluate values.
story = (f" {exclamation}! Bob said {adverb} as he stepped on the {noun}. Serves him right because he is an {adjective} ass. If only he went to the {nounTwo} instead. {exclamation}")

#printing the story
print(story)
