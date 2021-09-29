import random
def main():

    # sentence one
    word_one = get_determiner(quantity=1)
    noun_one = get_noun(quantity=1)
    verb_one = get_verb(quantity=1, tense="past")
    print(f"{word_one} {noun_one} {verb_one}.")

    # sentence two
    word_two = get_determiner(quantity=0)
    noun_two = get_noun(quantity=0)
    verb_two = get_verb(quantity=0, tense="past")
    print(f"{word_two} {noun_two} {verb_two}.")

    # sentence three
    word_three = get_determiner(quantity=1)
    noun_three = get_noun(quantity=1)
    verb_three = get_verb(quantity=1, tense="present")
    print(f"{word_three} {noun_three} {verb_three}.")

    # sentence four
    word_four = get_determiner(quantity=0)
    noun_four = get_noun(quantity=0)
    verb_four = get_verb(quantity=0, tense="present")
    print(f"{word_four} {noun_four} {verb_four}.")

    # sentence five
    word_five = get_determiner(quantity=1)
    noun_five = get_noun(quantity=1)
    verb_five = get_verb(quantity=1, tense="future")
    print(f"{word_five} {noun_five} {verb_five}.")

    # sentence six
    word_six = get_determiner(quantity=0)
    noun_six = get_noun(quantity=0)
    verb_six = get_verb(quantity=0, tense="future")
    print(f"{word_six} {noun_six} {verb_six}.")

    # with prepositional phrases
    # sentence seven
    word_seven = get_determiner(quantity=1)
    noun_seven = get_noun(quantity=1)
    verb_seven = get_verb(quantity=1, tense="past")
    preposition_one = get_prepositional_phrase(quantity=1).replace(",", "")
    print(f"{word_seven} {noun_seven} {verb_seven} {preposition_one}.")

    # sentence eight
    word_eight = get_determiner(quantity=0)
    noun_eight = get_noun(quantity=0)
    verb_eight = get_verb(quantity=0, tense="past")
    preposition_two = get_prepositional_phrase(quantity=0).replace(",", "")
    print(f"{word_eight} {noun_eight} {verb_eight} {preposition_two}.")

    # sentence nine
    word_nine = get_determiner(quantity=1)
    noun_nine = get_noun(quantity=1)
    verb_nine = get_verb(quantity=1, tense="present")
    preposition_three = get_prepositional_phrase(quantity=1).replace(",", "")
    print(f"{word_nine} {noun_nine} {verb_nine} {preposition_three}.")

    # sentence ten
    word_ten = get_determiner(quantity=0)
    noun_ten = get_noun(quantity=0)
    verb_ten = get_verb(quantity=0, tense="present")
    preposition_four = get_prepositional_phrase(quantity=0).replace(",", "")
    print(f"{word_ten} {noun_ten} {verb_ten} {preposition_four}.")

    # sentence eleven
    word_eleven = get_determiner(quantity=1)
    noun_eleven = get_noun(quantity=1)
    verb_eleven= get_verb(quantity=1, tense="future")
    preposition_five = get_prepositional_phrase(quantity=1).replace(",", "")
    print(f"{word_eleven} {noun_eleven} {verb_eleven} {preposition_five}.")

    # sentence twelve
    word_twelve = get_determiner(quantity=0)
    noun_twelve = get_noun(quantity=0)
    verb_twelve = get_verb(quantity=0, tense="future")
    preposition_six = get_prepositional_phrase(quantity=0).replace(",", "")
    print(f"{word_twelve} {noun_twelve} {verb_twelve} {preposition_six}.")
    print()
    # make it my own displayed sentences
    # sentence thirteen
    word_thirteen = get_determiner(quantity=0)
    noun_thirteen = get_noun(quantity=0)
    verb_thirteen = get_verb(quantity=0, tense="future")
    preposition_seven = get_prepositional_phrase(quantity=0).replace(",", "")
    place_or_thing_one = get_place_or_thing(quanitity=0)
    print(f"{word_thirteen} {noun_thirteen} {verb_thirteen} {preposition_seven} {place_or_thing_one}.")

    # sentence fourteen
    word_fourteen = get_determiner(quantity=1)
    noun_fourteen = get_noun(quantity=1)
    verb_fourteen = get_verb(quantity=1, tense="present")
    preposition_eight = get_prepositional_phrase(quantity=1).replace(",", "")
    place_or_thing_two = get_place_or_thing(quanitity=1)
    print(f"{word_fourteen} {noun_fourteen} {verb_fourteen} {preposition_eight} {place_or_thing_two}.")

    # sentence fifteen
    word_fifteen = get_determiner(quantity=0)
    noun_fifteen = get_noun(quantity=0)
    verb_fifteen = get_verb(quantity=0, tense="past")
    preposition_nine = get_prepositional_phrase(quantity=0).replace(",", "")
    place_or_thing_three = get_place_or_thing(quanitity=2)
    print(f"{word_fifteen} {noun_fifteen} {verb_fifteen} {preposition_nine} {place_or_thing_three}.")



def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is a word
    like "the", "a", "one", "two", "some", "many". If quantity == 1,
    this function will return either "the" or "one". Otherwise
    this function will return either "some" or "many".

    Parameter
        quantity: an integer. If quantity == 1, this function will
            return a determiner for a singular noun. Otherwise this
            function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["The", "One"]
    else:
        words = ["Some", "Many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):
    """Return a randomly chosen noun. If quantity == 1, this
    function will return one of these ten singular nouns:
        "adult", "bird", "boy", "car", "cat",
        "child", "dog", "girl", "man", "woman"
    Otherwise, this function will return one of these ten
    plural nouns:
        "adults", "birds", "boys", "cars", "cats",
        "children", "dogs", "girls", "men", "women"

    Parameter
        quantity: an integer that determines if the
            returned noun is singular or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    noun = random.choice(nouns)
    return noun

def get_verb(quantity, tense):
    if  tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]
    
    elif tense == "present" and quantity == 1:
        verbs = [ "drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]

    elif tense == "present" and quantity != 1:
        verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]

    elif tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb

def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
        "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"

    Return: a randomly chosen preposition.
    """

    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]

    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.

    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """

    preposition_one = get_preposition()
    determiner_one = get_determiner(quantity)
    noun_word = get_noun(quantity)

    sentence_one = (f"{preposition_one}, {determiner_one}, {noun_word}")
    return sentence_one

# make it my own function
def get_place_or_thing(quanitity):

    if quanitity == 1:
        thing_places = ["basketballs", "baseballs", "bats", "rackets", "books", "desks", "shoes", "longboards"]
    elif quanitity == 0:
        thing_places = ["basketball", "baseball", "bat", "racket", "book", "desk", "shoe", "longboard"]
    else:
        thing_places = ["Texas", "Washington", "Oregon", "Idaho", "Utah", "California", "Montana", "Wyoming", "Arizona"]

    thing_place = random.choice(thing_places)
    return thing_place

main()