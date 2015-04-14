# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Departamento
"""
#Se crea la clase Departamento
class Depto(models.Model):
    
    _name = 'equipment.depto' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres
    name = fields.Char(string="Departamento", required=True) # Campo a generarse en la tabla _name
        
    responsable_id = fields.Many2one("res.users",
                                    ondelete='set null',string="Responsable", index=True)
    sucursal_ids = fields.Many2many("equipment.sucursal",
                                    ondelete='set null',string="Sucursal", index=True)
       #departamentos_ids = fields.One2many('equipment.sucursal', 'deptos_id', string="Sucursal")