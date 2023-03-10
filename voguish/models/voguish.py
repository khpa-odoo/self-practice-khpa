from odoo import fields, models, api, exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta    

class Voguish(models.Model):
    _name = "voguish"
    _description = "Voguish Model"
    _order = "sequence,id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True)
    image = fields.Binary()
    category_id = fields.Many2one("voguish.categories", string="Category")
    outfit_tag = fields.Many2one("voguish.tag")
    tag_ids = fields.Many2many("voguish.tag", string="Tags")
    tag_count = fields.Integer(compute="_compute_tag_count")
    size_ids = fields.Many2many("voguish.size",required=True, string="Available Size(s)")
    description = fields.Text()
    brand = fields.Text()
    deposit_price = fields.Float(readonly=True,default=3000)
    rent_per_day = fields.Float(required=True, store=True)
    alter_outfit = fields.Boolean(default=True)
    availability_status = fields.Boolean(default=True)
    date_start = fields.Date()
    date_end = fields.Date()
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Seller",default=lambda self:self.env.user)
    sequence = fields.Integer()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'),('alterations', 'Alterations'),
        ('rented', 'Rented'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="new",required=True,copy=False,tracking = True)
    outfit_type = fields.Selection(
        selection=[('mid_length', 'Mid Length'),('bottom_wear', 'Bottom Wear'),
        ('full_length', 'Full Length')],
        help="What's the Status!",default="full_length",required=True,copy=False,tracking=True)
    total_rent = fields.Float(compute="_compute_total_rent")

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
    
    @api.depends('rent_per_day','date_start','date_end')
    def _compute_total_rent(self):
        for record in self:
            if(not record.date_start):
                record.date_start = fields.Date.today()
            if(not record.date_end):
                record.date_end = fields.Date.today() + relativedelta(days=3)
            if (record.date_end < fields.Date.today()):
                raise exceptions.ValidationError("Availability dates cannot be set in the past.")
            record.total_rent = record.rent_per_day*float((record.date_end-record.date_start).days)

    def action_rent(self):
        for record in self:
            record.state = 'rented'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'

    @api.depends('tag_ids')
    def _compute_tag_count(self):
        for record in self:
            record.tag_count = len(record.tag_ids)