from odoo import fields, models

class VoguishSize(models.Model):
    _name = "voguish.size"
    _description = "Outfit Sizes Model"

    name = fields.Char(required=True)
    