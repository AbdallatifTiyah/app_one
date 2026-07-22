from odoo import models, fields


class Owner(models.Model):
    _name = 'owner'
    _description = "Model Owner"

    name = fields.Char(required=True)
    phone = fields.Char()
    address = fields.Char()
    property_ids = fields.One2many('property','owner_id')

    _unique_name = models.Constraint(
        "UNIQUE(name)",
        "This name already exists!"
    )