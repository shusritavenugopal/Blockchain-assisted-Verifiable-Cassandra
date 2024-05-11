from web3 import Web3
from solcx import compile_source
class Blockchain:
    def __init__(self,host):
        self.host= host
        self.contract_id=None
        self.contract_interface=None
        self.abi=None
        self.bytecode=None
        self.contract_instance=None
        self.service_provider=None


    def set_merkle_root(self,merkle_root):
        # data owner set merkle root
        set_tx_hash = self.contract_instance.functions.setMerkleRoot(merkle_root).transact()
        set_tx_recipient = self.service_provider.eth.wait_for_transaction_receipt(set_tx_hash)

    def get_merkle_root(self):
        return self.contract_instance.functions.getMerkleRoot().call()

    def compile_contract(self):
        compiled_sol = compile_source(
            '''
            pragma solidity >0.5.0;
            contract Verify{
                string merkleRoot;

                function setMerkleRoot(string memory _merkleRoot) public {
                    merkleRoot=_merkleRoot;
                }

                function getMerkleRoot()view public returns (string memory){
                    return merkleRoot;
                }
            }
            ''',
            output_values=['abi', 'bin']
        )

        contract_id, contract_interface = compiled_sol.popitem()

        bytecode = contract_interface['bin']
        abi = contract_interface['abi']
        self.bytecode = bytecode
        self.abi=abi

    #specify service provider
    def deploy_contract(self):
        #'http://127.0.0.1:8545'
        w3 = Web3(Web3.HTTPProvider(self.host))
        self.service_provider=w3
        w3.eth.default_account = w3.eth.accounts[0]

        Verify = w3.eth.contract(abi=self.abi, bytecode=self.bytecode)

        deploy_tx_hash = Verify.constructor().transact()
        deploy_tx_receipt = w3.eth.wait_for_transaction_receipt(deploy_tx_hash)

        verify = w3.eth.contract(
            address=deploy_tx_receipt.contractAddress,
            abi=self.abi
        )
        self.contract_instance=verify
    ## Ethereum Blockchain End ##
