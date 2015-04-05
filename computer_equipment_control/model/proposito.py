# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Control
"""
#Se crea la clase Proposito
class Proposito(models.Model):
    
    _name = 'equipment.proposito' # String crea entidad tomado por odoo 

    description = fields.Text()# campo de tipo Text para almacenar strings multilineas