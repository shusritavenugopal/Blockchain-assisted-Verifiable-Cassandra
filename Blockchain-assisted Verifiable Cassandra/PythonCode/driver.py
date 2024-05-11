import hashlib
from db_provider_modified import Server
from data_owner_m import DataOwner
from adv_client import MaliciousClient
from query_client import QueryClient
from blockchain import Blockchain

if __name__ == '__main__':
    # Define Data
    data_provider = Server()
    data = {
        "k1": "sunday",
        "k2": "monday",
        "k3": "tuesday",
        "k4": "wednesday",
        "k5": "thursday",
        "k6": "friday",
        "k7": "saturday"
    }

    # Setup blockchain
    blockchain = Blockchain('http://127.0.0.1:8545')
    blockchain.compile_contract()
    blockchain.deploy_contract()

    # Setup Data Owner
    data_owner = DataOwner(data, data_provider, blockchain)
    data_owner.build_merkle_tree() # build a merkle tree on the Data Owner side
    data_owner.insert_data_to_server() # upload data to the server
    data_owner.upload_merkle_tree_to_server() # upload merkle tree to the server
    data_owner.upload_merkle_root_to_blockchain() # save merkle root

    print("Merkle Tree Structure")
    print("Number of leaf nodes on Merkle tree", data_provider.merkle_tree.get_leaf_count())
    for i in range(data_provider.merkle_tree.get_leaf_count()):
        print(f"The value of the leaf at {i} as a hex string:", data_provider.merkle_tree.get_leaf(i))
        print(f"The proof array contains a set of merkle sibling objects at {i} is ", data_provider.merkle_tree.get_proof(i))


    print("The merkle root of the tree as a hex string", data_provider.merkle_tree.get_merkle_root())

    # Query client
    query_client = QueryClient(data_provider, blockchain)
    key = "k1"
    value = query_client.query_by_key(key)
    leaf_value = f"{key}:{value}"
    leaf_hash = hashlib.sha256(f"{leaf_value}".encode()).hexdigest()  # Generate hash from leaf value
    k1_proofs = query_client.retrieve_verification_path_by_tree(0)

    print("Query client")
    print(value)
    print(leaf_hash)
    print(k1_proofs)

    if query_client.query_verification(k1_proofs, leaf_hash, blockchain.get_merkle_root()):
         print("Retrieved value is verified")
    else:
         print("Retrieved value is modified")

    k1_proofs = query_client.retrieve_verification_path_by_tree(0) # 0 means root path



    # Case when adversary exist
    adversary = MaliciousClient(data_provider)
    adversary.modify_data_by_key("k1", "february") # adversary changes the first key value pair
    # Query again to see if result is modified
    key_m = 'k1'
    value_m = query_client.query_by_key(key_m)
    leaf_value_m = f"{key_m}:{value_m}"
    leaf_hash_m = hashlib.sha256(f"{leaf_value_m}".encode()).hexdigest()  # Generate hash from leaf value
    k1_proofs_m = query_client.retrieve_verification_path_by_tree(0)
    print("This is a malicious attack scenario.")
    print("Tampered value", value_m)
    print("Hash value (tampered) of retrieved value from Cassandra database", leaf_hash_m)
    print("Proofs of the key being queried", k1_proofs_m)
    print(blockchain.get_merkle_root()) 
    if query_client.query_verification(k1_proofs_m, leaf_hash_m, blockchain.get_merkle_root()):
        print("Retrived value is verified")
    else:
        print("Retrived value is modified")
