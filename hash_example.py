import hashlib

text = "I am Satoshi Nakamoto"

for nonce  in range(20):
    input_data = text + str(nonce)

    h = hashlib.sha256(input_data.encode('utf-8'))

    print(f"{input_data} => {h.hexdigest()}")