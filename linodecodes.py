import pprint

sentence = "Linode is really cool"
words = sentence.split(' ')

for word in words:
    print ''.join(reversed(word)),
print "\n"

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
