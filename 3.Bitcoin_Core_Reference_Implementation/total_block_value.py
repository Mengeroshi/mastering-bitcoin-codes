from bitcoin.rpc  import RawProxy
p = RawProxy(None, None, None, 120)

blockheight = 277316

blockhash = p.getblockhash(blockheight)

block = p.getblock(blockhash)

transactions = block['tx']

block_value = 0

for txid in transactions:
    tx_value = 0
    raw_tx = p.getrawtransaction(txid)
    decoded_tx = p.decoderawtransaction(raw_tx)

    for ouput in decoded_tx['vout']:
        
        tx_value = tx_value + ouput['value']

    block_value = block_value + tx_value

print(f"Total block value {block_value}")

