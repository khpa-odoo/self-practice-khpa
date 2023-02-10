from odoo import fields, models

class VoguishCategories(models.Model):
    _name = "voguish.categories"
    _description = "Outfit Categories Model"

    name = fields.Char(required=True)