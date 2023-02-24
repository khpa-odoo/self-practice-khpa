from odoo import fields, models, api, exceptions
from datetime import datetime
from dateutil.relativedelta import relativedelta    

class Voguish(models.Model):
    _name = "voguish"
    _description = "Voguish Model"
    _order = "sequence,id desc"

    name = fields.Char(required=True)
    image = fields.Binary()
    category_id = fields.Many2one("voguish.categories", string="Category")
    tag_ids = fields.Many2many("voguish.tag", string="Tags")
    size_ids = fields.Many2many("voguish.size",required=True, string="Available Size(s)")
    description = fields.Text()
    brand = fields.Text()
    deposit_price = fields.Float(readonly=True,default=3000)
    rent_per_day = fields.Float(required=True, copy=False, store=True)
    alter_outfit = fields.Boolean(default=True)
    availability_status = fields.Boolean(default=True)
    date_start = fields.Date()
    date_end = fields.Date()
    sequence = fields.Integer()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string='State',
        selection=[('new', 'New'),('alterations', 'Alterations'),
        ('rented', 'Rented'), ('cancelled', 'Cancelled')],
        help="What's the Status!",default="new",required=True,copy=False)
    total_rent = fields.Float(compute="_compute_total_rent")

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
    
    @api.depends('rent_per_day','date_start','date_end')
    def _compute_total_rent(self):
        for record in self:
            if(not record.date_start):
                record.date_start = fields.Date.today()
            if(not record.date_end):
                record.date_end = fields.Date.today() + relativedelta(days=3)
            if (record.date_start < fields.Date.today()):
                raise exceptions.ValidationError("Availability dates cannot be set in the past.")
            record.total_rent = record.rent_per_day*float((record.date_end-record.date_start).days)

    def action_rent(self):
        for record in self:
            record.state = 'rented'

    def action_cancel(self):
        for record in self:
            record.state = 'cancelled'