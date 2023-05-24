import xmlrpc.client

# Set up the connection to the Odoo server
        # Set up the Odoo API connection
url = 'https://dsl1.odoo.com/'
db = 'dsl1'
username = 'kaur.kallas@gmail.com'
# Read the secret API key from non published file
with open('odoo.token', 'r') as file:
    file_content = file.read()
api_key = file_content

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, api_key, {})

# Set up the object for accessing the Odoo models
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Get the IDs of the clients who have made purchases
order_ids = models.execute_kw(db, uid, api_key, 'sale.order', 'search', [[['state', '=', 'sale']]])

# Get the clients who have made purchases
clients = []
for order_id in order_ids:
    order = models.execute_kw(db, uid, api_key, 'sale.order', 'read', [order_id])
    print(str(order))
    client_id = order[0]['partner_id'][0]
    client = models.execute_kw(db, uid, api_key, 'res.partner', 'read', [client_id])
    clients.append(client)

# Print the clients who have made purchases
for client in clients:
    print(client['name'])