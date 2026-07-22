from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Property(models.Model):
    _name = 'property'
    _description = "Model property"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(required=True, default='New')
    description = fields.Text(tracking=True)
    postcode = fields.Char(required=True)
    date_availability = fields.Date(tracking=True)
    excepted_price = fields.Float()
    selling_price = fields.Float()
    diff = fields.Float(compute='_compute_diff', store=False, readonly=False)
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ('north','North'),
        ('south','South'),
        ('east','East'),
        ('west','West'),
    ], default='north')
    owner_id = fields.Many2one('owner')
    tag_ids = fields.Many2many('tag')
    owner_address = fields.Char(related='owner_id.address', readonly=False)
    # owner_address = fields.Char(related='owner_id.address', readonly=False, store=True)
    owner_phone = fields.Char(related='owner_id.phone', readonly=False)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('sold', 'Sold'),
    ], default = 'draft')

    def action_draft(self):
        for rec in self:
            print("inside draft function")
            rec.state = 'draft'
           # rec.write({
           #     'state': 'draft'
           # })

    def action_pending(self):
        for rec in self:
            print("inside pending function")
            rec.state = 'pending'

    def action_sold(self):
        for rec in self:
            print("inside sold function")
            rec.state = 'sold'

    @api.depends('excepted_price', 'selling_price', 'owner_id.phone')
    def _compute_diff(self):
        for rec in self:
            print(rec)
            print("inside _compute_diff method")
            rec.diff = rec.excepted_price - rec.selling_price

    @api.onchange('excepted_price')
    def _onchange_excepted_price(self):
        for rec in self:
            print(rec)
            print("inside _onchange_excepted_price method")
            return {
                'warning': {
                    'title': 'Warning',
                    'message': 'Negative value',
                    'type': 'notification',
                }
            }

    _unique_name = models.Constraint(
        "UNIQUE(name)",
        "This name already exists!"
    )

    Line_ids = fields.One2many('property.line', 'property_id')

    # _sql_constraints = [
    #     ('unique_name','unique("name")','This name is exists!'),
    # ]


    # @api.constrains('bedrooms')
    # def _check_bedrooms_greater_zero(self):
    #     for rec in self:
    #         if rec.bedrooms == 0:
    #             raise ValidationError('Please add valid number of bedrooms!')
            

    # @api.model_create_multi
    # def create(self, vals):
    #     res = super(Property, self).create(vals)
    #     print("inside create method")
    #     return res
    
    # @api.model
    # def _search(self, domain, offset=0, limit=None, order=None):
    #     res = super(Property, self)._search(domain, offset=0, limit=None, order=None)
    #     print("inside search method")
    #     return res
    
    # def write(self, vals):
    #     res = super(Property, self).write(vals)
    #     print("inside write method")
    #     return res
    
    # def unlink(self):
    #     res = super(Property, self).unlink()
    #     print("inside unlink method")
    #     return res


class PropertyLine(models.Model):
    _name = 'property.line'
    _description = "Model property line"

    description = fields.Char()
    area = fields.Float()
    property_id = fields.Many2one('property')