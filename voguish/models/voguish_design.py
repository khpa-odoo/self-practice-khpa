from odoo import fields, models

class VoguishDesign(models.Model):
    _name = "voguish.design"
    _description = "Design Model"

    name = fields.Char(required=True)
    image = fields.Image()
    description = fields.Text()
    category_id = fields.Many2one("voguish.categories", string="Category")
    size = fields.Selection(
        selection=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'),('xl','XL'),('xxl','XXL')],
        help="Type is used to separate Leads and Opportunities")
    