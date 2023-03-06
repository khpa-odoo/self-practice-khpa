from odoo import fields, models

class VoguishDesign(models.Model):
    _name = "voguish.design"
    _description = "Design Model"
    _order = "id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    image = fields.Image(required=True)
    description = fields.Text()
    category_id = fields.Many2one("voguish.categories", string="Category")
    size = fields.Selection(
        selection=[('xs', 'XS'), ('s', 'S'), ('m', 'M'), ('l', 'L'),('xl','XL'),('xxl','XXL')])
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Seller",default=lambda self:self.env.user)
    state = fields.Selection(
        string='State',
        selection=[('designing', 'Designing'),('ready', 'Ready'),
        ('rented', 'Rented'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="designing",required=True,copy=False,tracking=True)
    outfit_type = fields.Selection(
        selection=[('mid_length', 'Mid Length'),('bottom_wear', 'Bottom Wear'),
        ('full_length', 'Full Length')],
        help="What's the Status!",default="full_length",required=True,copy=False,tracking=True)
    
    neck = fields.Float()
    neck_to_knee = fields.Float()
    bust = fields.Float()
    waist = fields.Float()
    hips = fields.Float() 
    arm_length = fields.Float()
    arm_hole = fields.Float()
    wrist = fields.Float()
    shoulder_to_waist = fields.Float()
    biceps = fields.Float()
    inseam = fields.Float()
    outseam = fields.Float()
    head_to_toe = fields.Float()
    
    def action_ready(self):
        for record in self:
            record.state = 'ready'

    def action_rent(self):
        for record in self:
            record.state = 'rented'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'
