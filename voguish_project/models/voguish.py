from odoo import models,Command

class Voguish(models.Model):
    _name = "voguish"
    _description = "Voguish Model"
    _inherit = 'voguish'

    def action_rent(self):
        values = {'name':self.name,'partner_id':self.buyer_id.id,'task_ids':[Command.create({"name":"Alteration"})]}
        self.env['project.project'].create(values)    
        return super().action_rent()