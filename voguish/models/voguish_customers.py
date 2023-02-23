from odoo import fields, models

class VoguishCustomers(models.Model):
    _name = "voguish.customers"
    _description = "Customers Model"

    name = fields.Char(required=True)