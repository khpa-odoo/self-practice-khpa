from odoo import fields, models

class Voguish(models.Model):
    _name = "voguish"
    _description = "Voguish Model"

    name = fields.Char(required=True)
    image = fields.Binary()
    category_id = fields.Many2one("voguish.categories", string="Category")
    tag_ids = fields.Many2many("voguish.tag", string="Tags")
    size_ids = fields.Many2many("voguish.size",required=True, string="Available Size(s)")
    description = fields.Text()
    brand = fields.Text()
    deposit_price = fields.Float(readonly=True,default=3000)
    rent_per_hour = fields.Float(readonly=True,copy=False)
    availability_status = fields.Boolean(default=True)
    date_start = fields.Date()
    date_end = fields.Date()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'), ('order received', 'Order Received'), 
        ('order accepted', 'Order Accepted'), ('alterations', 'Alterations'),
        ('rented', 'Rented'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="new",required=True,copy=False)
    

    neck = fields.Char()
    neck_to_knee = fields.Char()
    bust = fields.Char()
    waist = fields.Char()
    hips = fields.Char() 
    arm_length = fields.Char()
    arm_hole = fields.Char()
    wrist = fields.Char()
    shoulder_to_waist = fields.Char()
    biceps = fields.Char()
    inseam = fields.Char()
    