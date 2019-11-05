start_block_reward = 50

reward_interval = 210_000

def max_money():
    #50BTC = 5_000_000_000
    current_reward = 50 * 10**8
    total = 0
    while current_reward > 0:
        total += reward_interval * current_reward
        current_reward /= 2
    return total

print(f"Total BTC to ever be created {max_money()} satoshis")