# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Sucursal
"""
#Se crea la clase Control
class Sucursal(models.Model):
    
    _name = 'equipment.sucursal' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres

    name = fields.Char(string="Sucursal", required=True) # Campo a generarse en la tabla _name
    street = fields.Char(string="Street", required=True) # Campo a generarse en la tabla _name
    suburb = fields.Char(string="Suburb", required=True) # Campo a generarse en la tabla _name
    number = fields.Char(string="Numero") # Campo a generarse en la tabla _name
    
    responsible_id = fields.Many2one("res.users",
                                    ondelete='set null',string="Responsible", index=True)
    deptos_ids = fields.One2many('equipment.depto','sucursal_ids',string="Departamentos")
    #departamentos_ids = fields.One2many('equipment.sucursal', 'deptos_id', string="Sucursal")