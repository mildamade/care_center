from odoo import models, fields


class ProjectProject(models.Model):
    _inherit = "project.project"

    team_id = fields.Many2one(
        "crm.team",
        string="Project Team",
        domain=[("team_type", "in", ("support", "project"))],
    )
