from sentences import get_determiner, get_noun, get_preposition, get_prepositional_phrase, get_verb, get_place_or_thing
import pytest


def test_get_determiner():
    # Test the singular determiners.
    singular_determiners = ["The", "One"]
    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):
        word = get_determiner(1)

        # Verify that the word returned from get_determiner is
        # one of the words in the singular_determiners list.
        assert word in singular_determiners

    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.

    # Test the plural determiners.
    plural_determiners = ["Some", "Many"]
    for _ in range(4):
        word = get_determiner(2)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners

def test_get_noun():
    singular_nouns = ["adult", "bird", "boy", "car", "cat","child", "dog", "girl", "man", "woman"]

    for _ in range(20):
        noun = get_noun(1)

        assert noun in singular_nouns
    
    plural_nouns = ["adults", "birds", "boys", "cars", "cats","children", "dogs", "girls", "men", "women"]

    for _ in range(20):
        noun = get_noun(2)

        assert noun in plural_nouns

def test_get_verb():
    past_verbs = ["drank", "ate", "grew", "laughed", "thought","ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        verb = get_verb(1, "past")

        assert verb in past_verbs
    
    present_plural_verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        verb = get_verb(1, "present")

        assert verb in present_plural_verbs

    present_singular_and_plural_verbs = ["drink", "eat", "grow", "laugh", "think","run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        verb = get_verb(2, "present")

        assert verb in present_singular_and_plural_verbs

    future_verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run",
     "will sleep", "will talk", "will walk", "will write"]
    for _ in range(4):
        verb = get_verb(1, "future")

        assert verb in future_verbs

def test_get_prepositional():
    prepositions = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        
    for _ in range(4):
        preposition = get_preposition()

        assert preposition in prepositions

def test_get_prepositional_phrase():
    

    prepositions = [ "about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
        
    for _ in range(4):
        word = get_prepositional_phrase(1)
        word_define = word.split(", ")
        prepositional = word_define[0]
        assert prepositional in prepositions
    
    # singular test
    singular_nouns = ["adult", "bird", "boy", "car", "cat","child", "dog", "girl", "man", "woman"]

    for _ in range(4):
        word = get_prepositional_phrase(1)
        word_define = word.split(", ")
        noun_singular_part = word_define[2]

        assert noun_singular_part in singular_nouns


    singular_determiners = ["The", "One"]

    for _ in range(4):
        word = get_prepositional_phrase(1)
        word_define = word.split(", ")
        determiners_singular_part = word_define[1]

        assert determiners_singular_part in singular_determiners

    # plural test
    plural_nouns = ["adults", "birds", "boys", "cars", "cats","children", "dogs", "girls", "men", "women"]

    for _ in range(4):
        word = get_prepositional_phrase(2)
        word_define = word.split(", ")
        nouns_plural_part = word_define[2]
 
        assert nouns_plural_part in plural_nouns
    
    plural_determiners = ["Some", "Many"]

    for _ in range(4):
        word = get_prepositional_phrase(2)
        word_define = word.split(", ")
        determiners_plural_part = word_define[1]

        assert determiners_plural_part in plural_determiners  

# make it my own
def test_place_or_thing():
    plural_things = ["basketballs", "baseballs", "bats", "rackets", "books", "desks", "shoes", "longboards"]

    for _ in range(4):
        thing = get_place_or_thing(1)

        assert thing in plural_things
    
    singular_things = ["basketball", "baseball", "bat", "racket", "book", "desk", "shoe", "longboard"]

    for _ in range(4):
        thing = get_place_or_thing(0)

        assert thing in singular_things
    
    places = ["Texas", "Washington", "Oregon", "Idaho", "Utah", "California", "Montana", "Wyoming", "Arizona"]

    for _ in range(4):
        place = get_place_or_thing(2)

        assert place in places
    

pytest.main(["-v", "--tb=line", "-rN", "test_sentences.py"])