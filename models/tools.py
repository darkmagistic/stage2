from odoo import fields, models


class ToolOrder(models.Model):
    _name = "tool.order"
    _description = "stage2 database"

    tool_type = fields.Selection([
        ('extrusion_dies', 'EXTRUSION DIES'),
        ('moulds', 'MOULDS'), ('knives', 'KNIVES'),
        ('extrusion_former', 'EXTRUSION FORMERS'),
        ('cutting_tools', 'CUTTING TOOLS'),
        ('gauging_and_measuring', 'GAUGING AND MEASURING')
    ], string='tool_type', default='extrusion_dies')
    status = fields.Selection([
        ('quoted', 'QUOTED'),
        ('awaiting approval', 'AWAITING APPROVAL'),
        ('approved', 'APPROVED')
    ], string='Status', default='quoted')
    tool_reference = fields.Text(string="Tool_Reference", required=True)
    tool_weight_kg = fields.Float(string="Tool_Weight_Kg")
    tool_storage_location = fields.Text(string="Tool_Storage_Location")
    tool_drawing_pdf = fields.Binary(string="Tool_Drawing_Pdf")
    tool_drawing_dxf_dwg = fields.Binary(string="Tool_Drawing_dxf_dwg")
    image = fields.Binary(string="Image")
    tool_family = fields.Selection([
        ('square', 'Square'),
        ('rectangle', 'RECTANGLE'),
        ('d fender', 'D FENDER'),
        ('dd fender', 'DD FENDER'),
        ('b fender', 'B FENDER'),
        ('u channel', 'U CHANNEL')
    ], string='tool_family', default='square')
    Tool_diameter_mm = fields.Selection([
        ('75', '75'),
        ('150', '150'),
        ('200', '200')
    ], string='Tool_diameter_mm', default='75')
    design_diameter_mm = fields.Integer(string="Design_Diameter_Mm")
    bridge_fitted = fields.Selection([
        ('blank', 'BLANK'),
        ('yes', 'YES'),
        ('no', 'NO')
    ], string='bridge_fitted', default='blank')
