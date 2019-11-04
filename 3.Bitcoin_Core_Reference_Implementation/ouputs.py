from bitcoin.rpc import RawProxy
p = RawProxy()

#Alice txid
txid = "0627052b6f28912f2703066a912ea577f2ce4da4caa5a5fbd8a57286c345c2f2"

#get the rawtx in hex
raw_tx = p.getrawtransaction(txid)

#decode the tx hex in JSON
decoded_tx = p.decoderawtransaction(raw_tx)

#for every ouput prints the address and the value of it
for info in decoded_tx['vout']:
    print(info['scriptPubKey']['addresses'], info['value'])