from odoo import fields, models

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    type = fields.Selection([('national', 'National'), ('international', 'International')], string='Type')
    project_id = fields.Many2one('project.project', string='Project')
    lead_code = fields.Char(string='Lead Code', readonly=True, copy=False, default='New')
    user_partner_id = fields.Many2one('res.users', string='User Partner')
    is_tech = fields.Boolean(string='Is Tech')
