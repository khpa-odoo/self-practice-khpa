from odoo import fields, models

class VoguishTag(models.Model):
    _name = "voguish.tag"
    _description = "Outfit Tags Model"

    name = fields.Char(required=True)
    