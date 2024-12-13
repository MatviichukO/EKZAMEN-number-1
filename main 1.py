import hashlib

def sha256_hash(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    hex_digest = sha256.hexdigest()
    return hex_digest
message = "I love KUBG <3"
hash_value = sha256_hash(message)
print(f"SHA-256 hesh of my original text '{message}' is: {hash_value}")