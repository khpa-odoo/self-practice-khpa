from odoo import fields, models, api, exceptions

class VoguishTag(models.Model):
    _name = "voguish.tag"
    _description = "Outfit Tags Model"
    _sql_constraints = [
    ('check_tag_name_uniq', 'UNIQUE (name)', 'You can not have two outfit tags with the same name!')
    ]
    _order = "name desc"

    name = fields.Char(required=True)
    outfit_ids = fields.One2many('voguish', 'tag_ids',required=True)
    color = fields.Integer()
    
    @api.constrains('name')
    def _check_tag_unique_name(self):
        tag_ids = self.search([]) - self
        value = [x.name.lower() for x in tag_ids]
        if self.name and self.name.lower() in value:
            raise exceptions.ValidationError(('This tag already exists.'))
        return True
    