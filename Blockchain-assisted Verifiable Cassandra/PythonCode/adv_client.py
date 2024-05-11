
class MaliciousClient:

    def __init__(self, server):
        self.server = server

    # use add data function to modify data in the server
    def modify_data_by_key(self,key,new_value):
        self.server.add_data(key,new_value)
