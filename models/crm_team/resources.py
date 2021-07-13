from ..auth import odoo 
class crm_team_get():
    def get_team (data):
            odoo_client = odoo.OdooClient()
            uid, models = odoo_client.logging()
            venta = data["venta"]
            id_teamid = models.execute_kw(odoo_client.db, uid, odoo_client.password,
                            'crm.team', 'search_read',
                [[['name', '=', venta['name']]]],
                { 'fields': ['id'] ,'limit': 1})
            return id_teamid 

     


