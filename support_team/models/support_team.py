from odoo import fields, models


class SupportTeam(models.Model):
    _inherit = "crm.team"

    type_team = fields.Selection(
        [("sale", "Sale"), ("project", "Project"), ("support", "Support")],
        string="Type",
        default="support",
    )
