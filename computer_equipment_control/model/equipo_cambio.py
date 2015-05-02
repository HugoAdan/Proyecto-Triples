# -*- coding: utf-8 -*-
from openerp import api, exceptions, fields, models, _


"""
Este modulo crea el modelo Cambios
"""
#Se crea la clase Cambios
class Cambios(models.Model):

    _name = 'equipment.cambios'


    equipo_id =  fields.Integer(string="ID Equipo", readonly=True)


    tipo_id = fields.Char(string="Tipo de Equipo", readonly=True)
    duplicadotipo_id = fields.Char(string="Tipo de Equipo", readonly=True)



    ram = fields.Float(digits=(3, 3), help="Especificación en GB", string="RAM")
    duplicadoram = fields.Float(digits=(3, 3), help="Especificación en GB", string="RAM")
    
    

    dd = fields.Float(digits=(3, 0), help="Especificación de GB", string="Disco Duro")
    duplicadodd = fields.Float(digits=(3, 0), help="Especificación de GB", string="Disco Duro")

    
    procesador_id = fields.Char(string="Procesador", readonly=True)    
    duplicadoprocesador_id = fields.Char(string="Procesador", readonly=True)


    software_id = fields.Char(string="Sistema Operativo", readonly=True)
    duplicadosoftware_id = fields.Char(string="Sistema Operativo", readonly=True)


    programas_id = fields.Char(string="Programas", readonly=True)
    ducplicadoprogramas_id = fields.Char(string="Programas", readonly=True)
    

    responsible_id = fields.Char(string="Responsable del Equipo", readonly=True)
    duplicadoresponsible_id = fields.Char(string="Responsable del Equipo", readonly=True)