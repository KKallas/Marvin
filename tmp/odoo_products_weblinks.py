import odoo

# generate 3 empty variables into local execution space to keep autogenerated content compatiblity
db = None
uid = None
password = None

models = odoo.odooInterface()

# Quick sample:
#
product_ids = [12, 21, 20, 19]

# Fetch the base URL of the Odoo instance
base_url = models.execute_kw(db, uid, password, 'ir.config_parameter', 'get_param', ['web.base.url'])

# Generate the direct weblink to the product.product page for each product ID
for product_id in product_ids:
    product_link = f"{base_url}/web#id={product_id}&view_type=form&model=product.product&action= "
    print(f"Product ID: {product_id} - Link: {product_link}")

                