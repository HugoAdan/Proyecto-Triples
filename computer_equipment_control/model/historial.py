# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Historial
"""
#Se crea la clase Factura
class Historial(models.Model):
    
    _name = 'equipment.historial' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres
    equipoh_ids = fields.Many2one('equipment.control','historiale_ids', string="Historial")

    responsible_id = fields.Many2one("res.users",
                                    ondelete='set null',string="Usuario del equipo", index=True)
    

    #equipoh_ids = fields.Many2one('equipment.control','historiale_ids', string="Historial")

    #responsible_id = fields.Many2one("res.users",
     #                               ondelete='set null',string="Usuario del equipo", index=True)
	

	#Fecha de movimiento o cambio
	#Relaciones-----
	#Tipo de equipo
	#Responsable del equipo
	#Depto que pertenece
	#Sucursal