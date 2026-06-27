from odoo import models, fields


class Owner(models.Model):
    _name = 'tag'
    _description = "Model tag"

    name = fields.Char(required=True)