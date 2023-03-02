from odoo import models, Command

class Voguish(models.Model):
    _name = "voguish"
    _description = "Voguish Model"
    _inherit = 'voguish'

    def action_rent(self):
        values = {'partner_id':self.buyer_id.id,'move_type':'out_invoice','invoice_line_ids':[
            Command.create({
                "name": self.name,
                "quantity":1,
                "price_unit":self.total_rent
            }),
            Command.create({
                "name":"administrative fees",
                "quantity":1,
                "price_unit":100.00
            })
        ]}
        self.env['account.move'].create(values)
        return super().action_rent()