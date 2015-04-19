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
    
#Factura - Invoice
    folio = fields.Char(string="Folio", required=True) # Campo a generarse en la tabla _name
    provider = fields.Char(string="Proveedor", required=True) # Campo a generarse en la tabla _name
    date = fields.Date(string="Fecha", default=fields.Date.today) # Campo a generarse en la tabla _name

    usuarios_ids = fields.One2many('res.users','equipos_ids',string="Equipos")

    #historiale_ids = One2many('equipment.historial',
     #                              ondelete='set null',string="Equipo", index=True)


class Ram(models.Model):
    _name = 'equipment.ram'

    ram = fields.Char(string="Gigabits", required=True)




class Software(models.Model):
    _name = 'equipment.software'

    so = fields.Char(string="S.O", required=True)

    ofice = fields.Char(string="Office", required=True)




class OtrosDisp(models.Model):
    _name = 'equipment.otrosdisp'

    tipoimpresora = fields.Char(string="S.O", required=True)

    escaner = fields.Char(string="Office", required=True)

    combinacion = fields.Char(string="Office", required=True)
