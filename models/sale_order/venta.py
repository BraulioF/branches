from ..auth import odoo 

class saleOrder():
    """Odoo model: res.partner list for customer and company"""

    ##CREAR ORDER
    def order_create(data,idpatner,idteam):
        odoo_client = odoo.OdooClient()
        uid, models = odoo_client.logging()
        id = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order', 'create', 
            
            [{
            'partner_id': idpatner,
            'team_id' : idteam,
            'client_order_ref' : data['client_order_ref'],
            'partner_invoice_id' : data['partner_invoice_id'],
            'partner_shipping_id' : data['partner_shipping_id'],
            'payment_acquirer_id' : data['payment_acquirer_id'],
            'pricelist_id' : data['pricelist_id'],                              
            }])

        print("Quizas y solo Quizas esta sea la order_id", id)   
        name = models.execute_kw(odoo_client.db, uid, odoo_client.password, 'sale.order', 'name_get', [[id]])
        return id
class sale_order_coinsidencias():
    def get_coinsidencia (data,idteam):
            odoo_client = odoo.OdooClient()
            uid, models = odoo_client.logging()
            venta = data["venta"]
            team_details = models.execute_kw(odoo_client.db, uid, odoo_client.password,
                             'sale.order', 'search_read',
                [[['client_order_ref', '=', venta['client_order_ref']],['team_id', '=', idteam]]],
                { 'fields': ['name'] ,'limit': 20})
            return team_details 
    