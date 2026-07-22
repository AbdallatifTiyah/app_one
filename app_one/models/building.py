from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Building(models.Model):
    _name = 'building'
    _description = "building record"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'code'

    no = fields.Integer()
    code = fields.Char()
    description = fields.Text()
    name = fields.Char()
    active = fields.Boolean(string="Active", default=True)

