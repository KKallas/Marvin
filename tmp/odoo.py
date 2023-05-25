import xmlrpc.client
from discord import app_commands

class odooInterface:
    def __init__(self, user_var) -> None:
        global db, uid, password
        db = None
        uid = None
        password = None

        self.user_var = user_var

        # Set up the Odoo API connection
        self.url = 'https://dsl1.odoo.com/'
        self.db = 'dsl1'
        self.username = 'kaur.kallas@gmail.com'

        # Read the secret API key from non published file
        with open('odoo.token', 'r') as file:
            file_content = file.read()
        self.api_key = file_content
        self.password = self.api_key # for code compatibilty with chat GPT based answers

        # Endpoint for authentication
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.uid = self.common.authenticate(self.db, self.username, self.api_key, {})

        # Endpointfor queries
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    def execute_kw(self,in_db,in_uid,in_password,in_model,in_action,in_ctx=[[]],in_domain={}):
        return self.query_string("'"+str(in_model)+"','"+str(in_action)+"',"+str(in_ctx)+","+str(in_domain))

    def query_string(self,input_string):
        try:
            # Execute the query and return the result
            query = self.models.execute_kw(
                self.db,                # Odoo DB name
                self.uid,               # Odoo Username
                self.api_key,           # API_key for login
                eval(input_string)[0],  # Odoo model ie. product.product as string ''
                eval(input_string)[1],  # Odoo command [search,read,serach_read] -> find teh write ones as well
                eval(input_string)[2],  # Odoo search filters -> find an example
                eval(input_string)[3],  # Odoo output properties? {'fields': ['id', 'name']}
                )
            #print(query)
            return query
        except Exception as e:
            print(e)

"""
    def query(self,model,command,context,filters):
        query = models.execute_kw(db, uid, api_key,
    'product.product', 'search_read',
    [[]],
    {'fields': ['id', 'name']})

# Print the product names
for product in query:
    print(product['name'])

"""

if __name__ == '__main__':
    models = odooInterface(locals())
    #result = models.execute_kw(db, uid, password, 'product.product', 'search_read',[[]],{'fields': ['id', 'name']})
    #result = models.query_string("'product.product', 'search_read',[[]],{'fields': ['id', 'name']}")
    #for line in result:
    #    print(line['name'])

    # --- paste from chat-GPT ---
    
    # Search for contacts and retrieve their IDs
    contact_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[('is_company', '=', False)]])

    # Retrieve the contact details based on the IDs
    contacts = models.execute_kw(db, uid, password, 'res.partner', 'read', [contact_ids], {'fields': ['name', 'email', 'phone']})

    # Print the contacts
    for contact in contacts:
        print("Name:", contact['name'])
        print("Email:", contact['email'])
        print("Phone:", contact['phone'])
        print("-----")