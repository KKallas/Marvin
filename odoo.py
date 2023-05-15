import xmlrpc.client


class odooInterface:
    def __init__(self, user_var) -> None:
        self.user_var = user_var

        # Set up the Odoo API connection
        self.url = 'https://dsl1.odoo.com/'
        self.db = 'dsl1'
        self.username = 'kaur.kallas@gmail.com'

        # Read the secret API key from non published file
        with open('odoo.token', 'r') as file:
            file_content = file.read()
        self.api_key = file_content

        # Endpoint for authentication
        self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        self.uid = self.common.authenticate(self.db, self.username, self.api_key, {})

        # Endpointfor queries
        self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    def query_string(self,input_string):
        try:
            # Execute the query and return the result
            query = self.models.execute_kw(self.db, self.uid, self.api_key, eval(input_string)[0],eval(input_string)[1],eval(input_string)[2],eval(input_string)[3])
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
    o = odooInterface(locals())
    result = o.query_string("'product.product', 'search_read',[[]],{'fields': ['id', 'name']}")
    for line in result:
        print(line['name'])