import hashlib

hash_value = input('Enter a string to hash: ')

print(hashlib.algorithms_guaranteed)

hash_obj1 = hashlib.md5()
hash_obj1.update((hash_value.encode()))
print(hash_obj1.hexdigest())

hash_obj2 = hashlib.sha1()
hash_obj2.update((hash_value.encode()))
print(hash_obj2.hexdigest())

hash_obj3 = hashlib.sha224()
hash_obj3.update((hash_value.encode()))
print(hash_obj3.hexdigest())

hash_obj4 = hashlib.sha256()
hash_obj4.update((hash_value.encode()))
print(hash_obj4.hexdigest())

hash_obj5 = hashlib.sha512()
hash_obj5.update((hash_value.encode()))
print(hash_obj5.hexdigest())