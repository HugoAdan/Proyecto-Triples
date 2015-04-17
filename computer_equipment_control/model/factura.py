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
	provider = fields.Char(string="Provider", required=True) # Campo a generarse en la tabla _name
	date = fields.Date(default=fields.Date.today) # Campo a generarse en la tabla _name
	        
    responsable_id = fields.Many2one("res.users",
                                    ondelete='set null',string="Responsable", index=True)
    equipos_ids = fields.Many2many("equipment.control",
                                    ondelete='set null',string="Factura del Equipo", index=True)