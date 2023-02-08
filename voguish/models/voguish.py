from odoo import fields, models

class Voguish(models.Model):
    _name = "voguish"
    _description = "Voguish Model"

    name = fields.Char(required=True)
    description = fields.Text()
    brand = fields.Text()
    deposit_price = fields.Float(readonly=True,default=3000)
    rent_per_hour = fields.Float(readonly=True,copy=False)
    availability_status = fields.Boolean(default=True)
    date_availability = fields.Date("Available Till",readonly=True)
    category = fields.Selection(
        selection=[('casuals', 'Casuals'), ('chic', 'Chic'), ('formals', 'Formals'), ('ethnics', 'Ethnics')],
        help="Type is used to separate Leads and Opportunities")
    size = fields.Selection(
        selection=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'),('xl','XL'),('xxl','XXL')],
        help="Type is used to separate Leads and Opportunities")
    