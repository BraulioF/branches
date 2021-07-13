from ..auth import odoo 

class sale_order_line():
    """Odoo model: res.partner list for customer and company"""

    def order_line_create(data,order_id):
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        id = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order.line', 'create', 
            [{
                #"default_code" : line_create["default_code"],
                'order_id' : int(order_id),           
                "product_id" : int(data["product_id"]),
                "product_uom_qty": data["product_uom_qty"],
                "price_unit": data["price_unit"],  
                      
            }])

            
        #name = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order.line', 'name_get', [[id]])
        return id
    ##Buscar el default_code en la tabla product.template

    
