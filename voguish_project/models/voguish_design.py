from odoo import models,Command

class VoguishDesign(models.Model):
    _name = "voguish.design"
    _description = "Voguish Design Model"
    _inherit = 'voguish.design'

    def action_rent(self):
        values = {'name':self.name,'partner_id':self.buyer_id.id,'task_ids':[Command.create({"name":"Design Outfit"})]}
        self.env['project.project'].create(values)    
        return super().action_rent()