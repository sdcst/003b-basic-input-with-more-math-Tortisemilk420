#!python3
 
"""
Assignment 5:
Make a Mad Lib

Ask the user to enter a number of words, one for each of the underscored words in the following paragraph.  Once they have finished, display the following story to them with the replacements made in the Mad Lib

Today we picked apple from _PERSON_'s Orchard. I had no idea there were so many different varieties of apples. I ate _ADJECTIVE_ apples straight off the tree that tasted like _FOOD_. Then there was a _ADJECTIVE_ apple that looked like a _NOUN_.  When our bag was full, we went on a free hay ride to _PLACE_ and back. It ended at a hay pile where we got to _VERB_ _ADVERB_. I can hardly wait to get home and cook with the apples. We are going to make apple _FOOD_ and _THINGS_ pies!
"""
def mad_lib_story():

    person = input("Enter a name (PERSON): ")
    adjective1 = input("Enter an adjective (first ADJECTIVE): ")
    food1 = input("Enter a type of food (first FOOD): ")
    adjective2 = input("Enter another adjective (second ADJECTIVE): ")
    noun = input("Enter a noun: ")
    place = input("Enter a place: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")
    food2 = input("Enter another type of food (second FOOD): ")
    things = input("Enter a plural noun (THINGS): ")

    story = f"Today we picked apples from {person}'s Orchard. I had no idea there were so many different varieties of apples. " \
            f"I ate {adjective1} apples straight off the tree that tasted like {food1}. Then there was a {adjective2} apple " \
            f"that looked like a {noun}. When our bag was full, we went on a free hay ride to {place} and back. It ended at a " \
            f"hay pile where we got to {verb} {adverb}. I can hardly wait to get home and cook with the apples. We are going to " \
            f"make apple {food2} and {things} pies!"

    print("\nHere's your Mad Lib story:\n")
    print(story)

mad_lib_story()



