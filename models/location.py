from odoo import api. fields, models, _
from odoo.exceptions import UserError

class Location(models.Model):
    _name = "liga_drinks.location"
    name = fields.Char(string="Location name", required=False)
    address = fields.Char(string="Address", required=True)
    city = fields.Char(string="City", required=True, default="Campinas")
    delivery_fee = fields.Float(string="Delivery Fee", required=True, default=3)
    phone = fields.Char(string="Location phone", required=False)
    contacts_id = fields.Many2many('liga_drinks.contact', string='Customer')
    main_contact_id = fields.Many2one('liga_drinks.contact', string='Customer')
    note = fields.Char(string="Extra note about the location", required=False)

class Contact(models.Model):
#    _name = "liga_drinks.contact" acho q não vo precisar
    _inherit = "res.partner"

    location_id = fields.Many2many('liga_drinks.location', required=False)
    default_location_id = fields.One2one('liga_drinks.location', required=False)
