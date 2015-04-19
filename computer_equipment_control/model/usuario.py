# -*- coding: utf-8 -*-
from openerp import models,fields, _


"""
Este modulo crea el modelo Usuario
"""
#Se crea la clase Usuario
class Usuario(models.Model):
    
	_inherit = 'res.users'

	alias = fields.Char()

    
