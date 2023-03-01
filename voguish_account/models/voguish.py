from odoo import models,Command

class Voguish(models.Model):
    _name = "voguish"
    _description = "Estate Property Model"
    _inherit = 'voguish'

    def action_rent(self):
        print('---------------------------')
        return super().action_rent()