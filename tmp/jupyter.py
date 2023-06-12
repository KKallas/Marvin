from notebook.notebookapp import NotebookApp

class jupyter_iterface:
    def __init__(self) -> None:
        self.app = NotebookApp()
        self.app.initialize()

        # Add keyboard interrupt handler
        try:
            while True:
                self.app.start()
        except KeyboardInterrupt:
            pass
        # Set up the Odoo API connection
        # Todo, put this data into token as well
        #self.url = 'https://dsl1.odoo.com/'
        #self.db = 'dsl1'
        #self.username = 'kaur.kallas@gmail.com'

        # Read the secret API key from non published file
        #with open('odoo.token', 'r') as file:
        #    file_content = file.read()
        #self.api_key = file_content
        #self.password = self.api_key # for code compatibilty with chat GPT based answers

        # Endpoint for authentication
        #self.common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(self.url))
        #self.uid = self.common.authenticate(self.db, self.username, self.api_key, {})

        # Endpointfor queries
        #self.models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(self.url))

    #def execute_kw(self,in_db,in_uid,in_password,in_model,in_action,in_ctx=[[]],in_domain={}):
    #    return self.query_string("'"+str(in_model)+"','"+str(in_action)+"',"+str(in_ctx)+","+str(in_domain))

    #def query_string(self,input_string):
    #    try:
            # Execute the query and return the result
    #        query = self.models.execute_kw(
    #            self.db,                # Odoo DB name
    #            self.uid,               # Odoo Username
    #            self.api_key,           # API_key for login
    #            eval(input_string)[0],  # Odoo model ie. product.product as string ''
    #            eval(input_string)[1],  # Odoo command [search,read,serach_read] -> find teh write ones as well
    #            eval(input_string)[2],  # Odoo search filters -> find an example
    #            eval(input_string)[3],  # Odoo output properties? {'fields': ['id', 'name']}
    #            )
    #        return query
    #    except Exception as e:
    #        print(e)

    def boilerplate(self,action_name):
        try:
            with open("jupyter_"+action_name+".py", 'w') as file:
                header="""import jupyter

# dont know yet what

                """
                file.write(header)
                print("file written")
        except:
            print("An error occurred while writing the file.")

if __name__ == '__main__':
    jup = jupyter_iterface()
   