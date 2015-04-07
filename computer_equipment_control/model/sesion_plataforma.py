# -*- coding: utf-8 -*-
from openerp import api,models,fields, _


"""
Este modulo crea el modelo Sesion acceso de Plataforma
"""
#Se crea la clase Sesion
class Sesion(models.Model):
    
    _name = 'equipment.sesion' # String crea entidad tomado por odoo 

    plataform_user = fields.Char(string="Nombre", required=True) 
    plataform_username = fields.Char(string="Username", required=True)
    plataform_contrasena = fields.Char(string="Password", required=True)
    plataform_rango = fields.Char(string="Definir Rango de Usuario", required=True)