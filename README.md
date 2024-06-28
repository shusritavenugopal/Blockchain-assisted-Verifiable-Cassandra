# Cloud Computing Project - Blockchain Assisted Verifiable Cassandra

## Overview
This project focuses on creating a proof-of-concept system for secure data storage and retrieval in a distributed environment. The system involves key components such as Data Owner, Database Service Provider, Query Client, Malicious Client, Ethereum Blockchain, Cassandra, and Merkle Tree to demonstrate integrity verification using a local Merkle Hash Tree.

## Project Components
1. **Data Owner (DO):**
   - Responsible for preparing key-value data and constructing a local Merkle Hash Tree (MHT) over the data.
   - Implements a class `DataOwner` with methods `prepare_data(data)` and `build_mht(data)`.

2. **Database Service Provider (SP):**
   - Operates as a server hosting a Cassandra database for storing data received from the Data Owner.
   - Implements a class `DatabaseServiceProvider` with methods `store_data(data)` and `receive_data(data)`.

3. **Query Client (C):**
   - Issues key-value queries to the Database Service Provider and supports query issuance and result verification using the MHT.
   - Implements a class `QueryClient` with methods `issue_query(key)` and `verify_query_result(key, result, mht_root)`.

4. **Malicious Client (MC):**
   - Acts as an adversary to tamper with data stored in the Cassandra database.
   - Implements a class `MaliciousClient` with the method `tamper_data(data)`.

5. **Ethereum Blockchain:**
   - Utilized for additional security and verification purposes in the distributed system.

6. **Cassandra:**
   - Database technology used by the Database Service Provider for storing sensitive data.

7. **Merkle Tree:**
   - Employed for detecting data tampering and ensuring data integrity in distributed systems.

## Project Structure
- `data_owner.py`: Contains the DataOwner class for preparing data and building the Merkle Hash Tree.
- `database_service_provider.py`: Includes the DatabaseServiceProvider class for storing and receiving data in Cassandra.
- `query_client.py`: Implements the QueryClient class for issuing queries and verifying results using the MHT.
- `malicious_client.py`: Defines the MaliciousClient class for tampering with data in Cassandra.
- `README.md`: Project documentation providing an overview, components, and usage instructions.

## Usage
1. Clone the repository to your local machine.
2. Run the necessary Python scripts for each component:
   - `python data_owner.py`
   - `python database_service_provider.py`
   - `python query_client.py`
   - `python malicious_client.py`
3. Follow the prompts and instructions provided by each script to simulate the system's functionality.

## Conclusion
The Cloud Computing Project showcases a secure data storage and retrieval system with integrity verification mechanisms using Merkle Hash Trees, Ethereum Blockchain, and Cassandra. This project aims to demonstrate the importance of data integrity in distributed environments and the role of various components in ensuring secure data transactions.

For any inquiries or feedback, please contact:
- Bhavana Devulapally
- Shusrita Venugopal
- Neha Navarkar

Thank you for exploring our project!
