# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Sucursal
"""
#Se crea la clase Control
class Sucursal(models.Model):
    
    _name = 'equipment.sucursal' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres

    name = fields.Char(string="Sucursal", required=True)
    street = fields.Char(string="Calle", required=True) 
    suburb = fields.Char(string="Colonia", required=True)
    number = fields.Char(string="Numero", required=True) 
    
    responsible_id = fields.Many2one("res.users",
                                    ondelete='set null',string="Responsible", index=True)
    deptos_ids = fields.Many2many('equipment.depto','sucursal_ids',string="Departamentos")
    