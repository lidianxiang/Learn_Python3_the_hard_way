lexicon = {
    "north":"direction",
    "south":"direction",
    "east":"direction",
    "west":"direction",
    "go":"verb",
    "kill":"verb",
    "eat":"verb",
    "the":"stop",
    "of":"stop",
    "in":"stop",
    "bear":"noun",
    "princeness":"noun",
    "3":"number",
    "91234":"number",
    '1234':"number",
    "ASDFADFASDF":"error",
    "IAS":"error"
}

def scan(sentence):
    results = []
    words = sentence.split()
    for word in words:
        word_type = lexicon.get(word)
        results.append((word_type,word))
    return results

#
# lexicon = {
# 	'north': ('direction', 'north'),
# 	'south': ('direction', 'south'),
# 	'east': ('direction', 'east'),
# 	'west': ('direction', 'west'),
#
# 	'go': ('verb', 'go'),
# 	'kill': ('verb', 'kill'),
# 	'eat': ('verb', 'eat'),
#
# 	'the': ('stop', 'the'),
# 	'in': ('stop', 'in'),
# 	'of': ('stop', 'of'),
#
# 	'bear': ('noun', 'bear'),
# 	'princess': ('noun', 'princess'),
#     1234:('number',1234),
#     '3':('number',3),
#     '91234':('number',91234),
#     'ASDFADFASDF':('error','ASDFADFASDF')
# 	}
#
# def isnum(Num):
# 	try:
# 		return int(Num)
# 	except:
# 		return None
#
#
# def scan(sentence):
# 	words = sentence.split()
# 	result = []
#
# 	for word in words:
# 		if isnum(word):
# 			result.append(('number', int(word)))
# 		elif word in lexicon.keys():
# 			result.append(lexicon[word])
# 		else:
# 			result.append(('error', word))
# 	return result
