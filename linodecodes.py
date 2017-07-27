import pprint

def reverse_words(sentence):
    words = sentence.split(' ')
    reversified = ''

    for word in words:
        reversified = reversified + ''.join(reversed(word)) + " "

    return reversified

sentence = "Linode is really cool"
print reverse_words(sentence)

first_hash = {
	'data': {
		'cpu': [1, 1, 42, 20],
		'mem': [100, 100, 125, 90],
		'disk': {
			'read': [0, 40, 10, 4],
			'write': [224, 98, 70, 200],
			'swap': 0
		}
	},
	'foo': 11,
    'fiz': [1, 2]
}

second_hash = {
	'data': {
		'cpu': [5, 6],
		'disk': {
			'read': [100],
			'write': [100, 110, 120, 130, 140],
			'swap': 1
		},
		'net': [20, 30, 40]
	},
	'foo': 0,
	'bar': 19,
    'fiz': [3, 4]
}

def merge_hashes(first_hash, second_hash):
    merged_hash = {}

    for key in second_hash:
        if isinstance(second_hash[key], basestring) or isinstance(second_hash[key], int):
            merged_hash[key] = second_hash[key]
        elif isinstance(second_hash[key], list):
            if key in first_hash and key in second_hash:
                merged_hash[key] = first_hash[key] + second_hash[key]
            else:
                merged_hash[key] = second_hash[key]
        elif isinstance(second_hash[key], dict):
            merged_hash[key] = merge_hashes(first_hash[key], second_hash[key])

    first_hash_keys = list(set(first_hash.keys()) - set(second_hash.keys()))

    for key in first_hash_keys:
        merged_hash[key] = first_hash[key]


    return merged_hash

pprint.pprint(merge_hashes(first_hash, second_hash), width=1)

a = [80,93,17,64,93,17,41,86,8,51,69,4,27,75,49,56,95,8,16,2,73,34,85,89,96,39,99,64,13,94,93,25,76,11,26,91,85,28,11,55,9,36,68,96,23,53,66,90,68,79,17,68,85,91,49,94,90,16,96,74,9,69,84,14,99,50,15,90,13,3,17,64,26,48,68,99,99,50,91,91,89,93,36,22,67,43,90,49,76,34,16,80,29,18,53,27,33,71,37,62]

def find_dupes(a):
    seen = set()
    dupes = set()

    for x in a:
        if x in seen:
            dupes.add(x)
        else:
            seen.add(x)

    return list(dupes)

print find_dupes(a)

def print_permutations(string, position = 0):

    if position == len(string):
        print "".join(string)

    for i in range(position, len(string)):

        string_copy = [character for character in string]
        string_copy[position], string_copy[i] = string_copy[i], string_copy[position]
        print_permutations(string_copy, position + 1)

print_permutations('cat')

list1 = ['d','i','q','z','e','f','v','p','s','o','u','k','l','g','h','w','a','m','j','n','c','y','t','x','r','b']
list2 = ['a','have','reward','end','sentencing','proving','words','the','not','sorry','clever','sorted','the','that','you','are','this','lists','correctly','but','be','the','more','hard','was','should']

def sort_linked_lists(list1, list2):
    sorted_tuples = sorted(zip(list1, list2), key=lambda tup: tup[0])
    return zip(*sorted_tuples)[1]

print sort_linked_lists(list1, list2)
