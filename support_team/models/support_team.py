from odoo import fields, models


class SupportTeam(models.Model):
    _inherit = "crm.team"

    team_type = fields.Selection(
        selection_add=[("project", "Project"), ("support", "Support")]
    )
