# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Factura
"""
#Se crea la clase Factura
class Factura(models.Model):
    
    _name = 'equipment.factura' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres
    folio = fields.Char(string="Folio", required=True) # Campo a generarse en la tabla _name
	proveedor = fields.Char(string="Proveedor", required=True) # Campo a generarse en la tabla _name
	fecha = fields.Date(string="Fecha", required=True) # Campo a generarse en la tabla _name