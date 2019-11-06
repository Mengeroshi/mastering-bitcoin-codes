import hashlib
import time



max_nonce = 2**32

def proof_of_work(header, difficulty_bits):
    target = 2**(256-difficulty_bits)

    for nonce in range(max_nonce):
        input_data = str(header) + str(nonce)
        h = hashlib.sha256(input_data.encode('utf-8'))
        hash_result = h.hexdigest()

        if int(hash_result, 16) < target:
            print(f"Success with nonce {nonce}")
            print(f"Hash is {hash_result}")
            return(hash_result, nonce)

    print(f"Failed after {max_nonce} tries")
    return nonce

if __name__ == '__main__':
    nonce = 0
    hash_result = ''

    for difficulty_bits in range(32):
        difficulty = 2 ** difficulty_bits
        print("Difficulty: %ld (%d bits)" %(difficulty, difficulty_bits) )
        print("Starting Search...")

        start_time = time.time()

        # make a new block which includes the hash from the previous block
        # we fake a block of transactions - just a string
        new_block = 'test block with transactions' + hash_result
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)

        end_time = time.time()

        elapsed_time = end_time - start_time
        print("Elapsed Time: %.4f seconds" %elapsed_time)

        if elapsed_time > 0:
            hash_power = float(int(nonce) / elapsed_time)
            print(f"Hashing Power: {hash_power} hashes per second")
