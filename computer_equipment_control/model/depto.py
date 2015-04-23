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
    asigndisp = fields.Selection([
         ('imprnormal', "Impresora"),
         ('impretiquetas', "Impresora de Etiquetas"),
         ('copiadora', "Copiadora"),
         ('imprescaner', "Impresora y Scanner"),
         ('scaner', "Scanner"),
    ], required = True, string="Dispositivo Externo")


    sucursal_ids = fields.Many2many("equipment.sucursal",
                                    ondelete='set null',string="Sucursal", index=True)