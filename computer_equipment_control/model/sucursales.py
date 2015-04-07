# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Sucursal
"""
#Se crea la clase Control
class Sucursal(models.Model):
    
    _name = 'equipment.sucursal' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres

    sucursal = fields.Char(string="Sucursal", required=True) # Campo a generarse en la tabla _name
    ubicacion_sucursal = fields.Char(string="Ubicacion", required=True) # Campo a generarse en la tabla _name
    numero_sucursal = fields.Integer(string="Numero", required=True) # Campo a generarse en la tabla _name