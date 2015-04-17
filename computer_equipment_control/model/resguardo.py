# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Resguardo
"""
#Se crea la clase Rescuardo
class Resguardo(models.Model):
    
    _name = 'equipment.resguardo' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres
        
   