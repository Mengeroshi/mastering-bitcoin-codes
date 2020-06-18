import hashlib

text = "I am Satoshi Nakamoto"

for nonce  in range(20):
    input_data = text + str(nonce)

    h = hashlib.sha256(input_data.encode('utf-8'))

    print(f"{input_data} => {h.hexdigest()}")


preimage = 'hashger'
sha256_hash = hashlib.sha256(preimage.encode('utf-8'))

print(f'{preimage} => {sha256_hash.hexdigest()}')

h = hashlib.new('ripemd160')

h.update(b"Nobody inspects the spammish repetition")

print(f'leeeeel => {h.hexdigest()}')