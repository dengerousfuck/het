import memcache

cache = memcache.Client(['127.0.0.1:11211'],debug=True)


def set(key,value,timeout=60):
    cache.set(key, value, timeout)
    print('--'*80)
    print(cache.get(key))
    return cache.set(key,value,timeout)

def get(key):
    return cache.get(key)

def delete(key):
    return cache.delete(key)