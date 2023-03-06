from odoo import fields,models

class ResUsers(models.Model):
    _inherit = "res.users"

    outfit_ids = fields.One2many("voguish","salesperson_id",domain = [('state','=','rented')])
    custom_outfit_ids = fields.One2many("voguish.design","salesperson_id",domain = [('state','=','rented')])