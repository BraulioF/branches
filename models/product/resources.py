from ..auth import odoo 
class ResProductGet():
    def get_default_code (data):
            odoo_client = odoo.OdooClient()
            uid, models = odoo_client.logging()
            product = data["producto"]
            parners_details = models.execute_kw(odoo_client.db, uid, odoo_client.password,
                            'product.template', 'search_read',
                [[['default_code', '=', product["default_code"]]]],
                { 'fields': ['default_code'] ,'limit': 1})
            return parners_details 