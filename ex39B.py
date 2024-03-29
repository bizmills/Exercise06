def Map(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def Map_hash(aMap, key):
    """Given a key this will create a number and then convert it to and index for the aMap's buckets."""
    return hash(key) % len(aMap)

def Map_get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = Map_hash(aMap, key)
    return aMap[bucket_id]

def Map_get_slot(aMap, key, default=None):
    """Returns the index, key, and value of a slot found in a bucket."""
    bucket = Map_get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v

    return -1, key, default

def Map_get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = Map_get_slot(aMap, key, default=default)
    return v

def Map_set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = Map_get_bucket(aMap, key)
    i, k, v = Map_get_slot(aMap, key)

    if v:
        bucket[i] = (key, value)
    else:
        bucket.append((key, value))


def Map_delete(aMap, key):
    """Deletes the given key from the map."""
    bucket = Map_get_bucket(aMap, key)

    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def Map_list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v

# The tests that it will work.

jazz = Map()
Map_set(jazz, 'Miles Davis', 'Flemenco Sketches')
# confirms set will replace previous one
Map_set(jazz, 'Miles Davis', 'Kind of Blue')
Map_set(jazz, 'Duke Ellington', 'Beginning To See The Light')
Map_set(jazz, 'Billy Strayhorn', 'Lush Life')

print "---- List Test ----"
Map_list(jazz)

print "---- Get Test ----"
print Map_get(jazz, 'Miles Davis')
print Map_get(jazz, 'Duke Ellington')
print Map_get(jazz, 'Billy Strayhorn')

print "---- Delete Test----"
print "** Goodbye Miles"
Map_delete(jazz, "Miles Davis")
Map_list(jazz)

print "** Goodbye Duke"
Map_delete(jazz, "Duke Ellington")
Map_list(jazz)

print "** Goodbye Billy"
Map_delete(jazz, "Billy Strayhorn")
Map_list(jazz)

print "** Goodbye Pork Pie Hat"
Map_delete(jazz, "Charles Mingus")