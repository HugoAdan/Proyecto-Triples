# -*- coding: utf-8 -*-
from openerp import api, exceptions, fields, models, _


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
    

    dispexternos_id = fields.Many2many("equipment.dispositivosexternos",
                                    ondelete='set null',string="Dispositivos Externos", index=True)

    sucursal_ids = fields.Many2many("equipment.sucursal",
                                    ondelete='set null',string="Sucursal", index=True)
    


class DispositivosExternos(models.Model):
    
    _name = 'equipment.dispositivosexternos'

    name = fields.Char(readonly = True,compute="_get_full_dispositivo_externo")
    externo_name =  fields.Char(string="Nombre", required=True, default="Dispositivo Externo")
    marca = fields.Char(string="Marca", required=True, default="Marca")
    descripcion = fields.Char(string="Descripcion", required=True, default="")
    
    
 
    @api.one
    @api.depends("externo_name", "marca")
    def _get_full_dispositivo_externo(self):
        self.name = str(self.externo_name) + " " +str(self.marca)

   