import hashlib
from blockchain import Blockchain
from db_provider import Server
from data_owner import DataOwner
import merkletools
from adv_client import MaliciousClient

# This class serves as a query client and also performs verification
class QueryClient:

    def __init__(self, server, blockchain):
        self.server = server
        self.blockchain = blockchain

    # Perform query to server
    def query_by_key(self, key):
        return self.server.get_data(key)

    # Get proof from server's Merkle tree
    def retrieve_verification_path_by_tree(self, key_index):
        return self.server.merkle_tree.get_proof(key_index)

    # Get Merkle root from blockchain
    def retrieve_root_from_blockchain(self):
        return self.blockchain.get_merkle_root()

    # Query clients issue query verifications
    def query_verification(self, proofs, retrieved_value, root_from_contract):
        return self.server.merkle_tree.validate_proof(proofs, retrieved_value, root_from_contract)
