from nose.tools import *
from ex48 import lexicon,parser

def test_subject():
    s1 = parser.Sentence(('noun',"cheese"),
                        ('verb',"eats"),
                        ('noun',"pigeon"))
    assert s1.verb == "eats"
    assert s1.subject == "cheese"
    assert s1.object == "pigeon"

def test_peek():
    word_list = []
    assert None == parser.peek(word_list)

    word_list = lexicon.scan("princess kill bear")
    assert_equal("noun",parser.peek(word_list))

def test_match():
    word_list = []
    assert None == parser.match(word_list,'noun')

    word_list = lexicon.scan("bear eat princess")
    assert_equal(('noun','bear'),parser.match(word_list,'noun'))
    assert_equal(None,parser.match(word_list,'noun'))
