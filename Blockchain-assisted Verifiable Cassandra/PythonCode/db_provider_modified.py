from cassandra.cluster import Cluster
import uuid
import base64

class Server:
    def __init__(self):
        self.cluster = Cluster()
        self.session = self.cluster.connect()
        self.merkle_tree = None
        self.keyspace = "project3"  # keyspace(database) name for storing data
        self.table = "data"  # table name for storing data
        self.treetable = "merkle"

        # Create keyspace and corresponding table if they don't exist
        self.session.execute(
            f"CREATE KEYSPACE IF NOT EXISTS {self.keyspace} WITH REPLICATION = {{'class' : 'SimpleStrategy', 'replication_factor' : 1}}"
        )
        self.session.set_keyspace(self.keyspace)
        self.session.execute(
            f"CREATE TABLE IF NOT EXISTS {self.table} (key text PRIMARY KEY, value text)"
        )
        # self.session.execute(f"CREATE TABLE IF NOT EXISTS {self.treetable} (id UUID PRIMARY KEY, root_hash text);")

    def add_data(self, key, value):
        # Insert data into the table
        self.session.execute(f"INSERT INTO {self.table} (key, value) VALUES (%s, %s)", (key, value))

    def get_data(self, key):
        # Retrieve value by key
        result = self.session.execute(f"SELECT value FROM {self.table} WHERE key = %s", (key,))
        if result:
            value = result.one().value
            return (value) #value_hex
        else:
            return None

