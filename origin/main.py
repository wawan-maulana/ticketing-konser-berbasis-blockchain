from blockchain import Blockchain

blockchain = Blockchain()

blockchain.add_block({
    "event": "Conser Musik Indie 2026",
    "token_id": "NFT-TIX-001",
    "contract_address": "0xSmartContractTicket123",
    "actor": "Promotor",
    "action": "Mint NFT Ticket",
    "face_value": "Rp 500.000",
    "max_resale_price": "Rp 550.000"
})

blockchain.add_block({
    "event": "Conser Musik Indie 2026",
    "token_id": "NFT-TIX-001",
    "actor": "Smart Contract Protocol",
    "action": "Enforce Anti-Scalping Rule",
    "status": "Verified & Immutable",
    "description": "Menolak duplikasi token dan mengunci aturan batas harga jual sekunder."
})

blockchain.add_block({
    "event": "Conser Musik Indie 2026",
    "token_id": "NFT-TIX-001",
    "actor": "Primary Buyer",
    "owner_wallet": "0xWalletBuyerA111",
    "action": "Purchase Ticket",
    "price_paid": "Rp 500.000"
})

for block in blockchain.chain:
    print("=" * 50)
    print("INDEX :", block.index)
    print("DATA  :", block.data)
    print("PREV  :", block.previous_hash)
    print("HASH  :", block.hash)

print("\nBlockchain valid:", blockchain.is_valid())