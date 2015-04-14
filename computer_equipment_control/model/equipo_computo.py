# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Control
"""
#Se crea la clase Control
class Control(models.Model):
    
    _name = 'equipment.control' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres

    tipo = fields.Char(string="Tipo", required=True) # Campo a generarse en la tabla _name
    ram = fields.Char(string="RAM", required=True) # Campo a generarse en la tabla _name
    dd = fields.Char(string="Disco Duro", required=True) # Campo a generarse en la tabla _name
    procesador = fields.Char(string="Procesador", required=True) # Campo a generarse en la tabla _name
    so = fields.Char(string="Sistema Operativo", required=True) # Campo a generarse en la tabla _name
    ofice = fields.Char(string="Office", required=True) # Campo a generarse en la tabla _name

    responsible_id = fields.Many2one("res.users",
                                    ondelete='set null',string="Responsable del Equipo", index=True)    