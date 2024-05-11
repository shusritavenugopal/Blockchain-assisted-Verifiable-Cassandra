from db_provider_modified import Server
from merkletools import MerkleTools
import base64

class DataOwner:
    def __init__(self, key_value_data, server, blockchain):
        self.data = key_value_data
        self.server = server
        self.merkle_tree = None
        self.blockchain = blockchain

    def insert_data_to_server(self):
        # Insert data to the server
        for key, value in self.data.items():
            self.server.add_data(key, value)

    def build_merkle_tree(self):
        mt = MerkleTools()
        for key, value in self.data.items():
            # Concatenate key and value with a separator
            leaf_value = f"{key}:{value}"
            # Add the leaf to the Merkle tree
            print(leaf_value)
            mt.add_leaf(leaf_value, True)

        # Make the Merkle tree ready
        mt.make_tree()
        self.merkle_tree = mt
        print("Merkle root:", mt.get_merkle_root())

    def upload_merkle_tree_to_server(self):
        # Upload the Merkle tree root hash to the server
        self.server.merkle_tree = self.merkle_tree
        print(self.server.merkle_tree)

    def get_merkle_root(self):
        # Get the Merkle root
        return self.merkle_tree.get_merkle_root() # 00edef87008946b63cf8707b209ec7335d7d14ca8478a26ccbaab08f2940c657

    def upload_merkle_root_to_blockchain(self):
        # Upload the Merkle root to the blockchain
        # self.blockchain.upload_merkle_root(self.get_merkle_root())
        self.blockchain.set_merkle_root(self.get_merkle_root())