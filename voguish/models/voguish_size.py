from odoo import fields, models, api, exceptions

class VoguishSize(models.Model):
    _name = "voguish.size"
    _description = "Outfit Sizes Model"
    _sql_constraints = [('check_size_name_uniq', 'UNIQUE (name)', 'You can not have two outfit sizes with the same name!')]
    

    name = fields.Char(required=True)
    
    @api.constrains('name')
    def _check_size_unique_name(self):
        size_ids = self.search([]) - self
        value = [x.name.lower() for x in size_ids]
        if self.name and self.name.lower() in value:
            raise exceptions.ValidationError(('This size already exists.'))
        return True
    