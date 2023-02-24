from odoo import fields, models, api, exceptions

class VoguishCategories(models.Model):
    _name = "voguish.categories"
    _description = "Outfit Categories Model"
    _sql_constraints = [('check_ctg_name_uniq', 'UNIQUE (name)', 'You can not have two outfit categories with the same name!')]
    _order = "id desc"

    name = fields.Char(required=True)
    category_ids = fields.One2many('voguish','category_id')

    @api.constrains('name')
    def _check_ctg_unique_name(self):
        ctg_ids = self.search([]) - self
        value = [x.name.lower() for x in ctg_ids]
        if self.name and self.name.lower() in value:
            raise exceptions.ValidationError(('This category already exists.'))
        return True
    