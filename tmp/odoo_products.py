import odoo

# generate 3 empty variables into local execution space to keep autogenerated content compatiblity
db = None
uid = None
password = None

models = odoo.odooInterface()

# Quick sample:
#
result = models.execute_kw(db, uid, password, 'product.product', 'search_read',[[]],{'fields': ['id', 'name']})

print(str(result))

                