from odoo import models, fields


class Owner(models.Model):
    _name = 'tag'

    name = fields.Char(required=True)