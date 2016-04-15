# Version 2.7 to 3.5: print(), use {}/.format() instead of % foramtters.
# dicts (dictionaries) continued...
# for Exercise 39_test

# Creating a dictionary module
def new(num_buckets=256):
	"""Initializes a Map with a given number of buckets."""
	aMap = []
	for i in range(0, num_buckets):
		aMap.append([])
	return aMap

def hash_key(aMap, key):
	"""Given a key this will create a numeric index for the 
	aMap buckets running along the length of aMap."""
	return hash(key) % len(aMap)
	
def get_bucket(aMap, key):
	"""Given a key, find the associated bucket."""
	bucket_id = hash_key(aMap, key)
	return aMap[bucket_id]
	
def get_slot(aMap, key, default = None):
	"""
	Returns the index, key and value of a slot within a bucket.
	Will return -1, key and default (None if not specifically set)
	when not found.
	"""
	bucket = get_bucket(aMap, key)
	
	for i, kv in enumerate(bucket):
		k, v = kv
		if key == k:
			return i, k, v
			
	return -1, key, default
	
def get(aMap, key, default = None):
	"""
	Gets the value in a bucket for the hiven key or returns
	the default.
	"""
	i, k, v = get_slot(aMap, key, default = default)
	return v
	
def set(aMap, key, value):
	"""
	Sets a new key for a value, replacing any existing value.
	"""
	bucket = get_bucket(aMap, key)
	i, k, v = get_slot(aMap, key)
	
	# if the key exists, replace it...
	if i >= 0:
		bucket[i] = (key, value)
	# if not, append to create it...
	else:
		bucket.append((key, value))
	
def delete(aMap, key):
	""" Deletes a given key from the Map."""
	bucket = get_bucket(aMap, key)
	
	for i in xrange(len(bucket)):
		k, v = bucket[i]
		if key == k:
			del bucket[i]
			break
			
def list(aMap):
	""" Prints out map contents."""
	for bucket in aMap:
		if bucket:
			for k, v in bucket:
				print(k, v)
	
