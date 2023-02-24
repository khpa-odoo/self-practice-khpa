from odoo import fields, models

class VoguishCustomers(models.Model):
    _name = "voguish.customers"
    _description = "Customers Model"

    name = fields.Char(required=True)
    partner_id = fields.Many2one('res.partner', string='Company', required=True)
    email = fields.Char(related='partner_id.email', store=True, readonly=False)
    phone = fields.Char(related='partner_id.phone', store=True, readonly=False)
    mobile = fields.Char(related='partner_id.mobile', store=True, readonly=False)
    website = fields.Char(related='partner_id.website', readonly=False)
    