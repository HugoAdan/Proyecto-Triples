# -*- coding: utf-8 -*-
from openerp import api, exceptions, fields, models, _

"""
Este modulo crea el modelo Control
"""
#Se crea la clase Control
class Control(models.Model):
    
    _name = 'equipment.control' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres
    
    tipo_id = fields.Many2one("equipment.tipo",
                                    ondelete='set null',string="Tipo de Equipo", index=True)

    ram = fields.Float(digits=(3, 3), help="Especificación en GB", string="RAM")
    dd = fields.Float(digits=(3, 0), help="Especificación de GB", string="Disco Duro")

    procesador_id = fields.Many2one("equipment.procesador",
                                    ondelete='set null',string="Procesador", index=True)
    
    software_id = fields.Many2one("equipment.software",
                                    ondelete='set null',string="Sistema Operativo", index=True)

    office_id = fields.Many2one("equipment.office",
                                    ondelete='set null',string="Office", index=True)


    responsible_id = fields.Many2one("res.users",
                                    ondelete='set null',string="Responsable del Equipo", index=True)
    
#Factura - Habilitar)
    folio = fields.Char(string="Folio", required=True) # Campo a generarse en la tabla _name
    provider = fields.Char(string="Proveedor", required=True) # Campo a generarse en la tabla _name
    date = fields.Date(string="Fecha", default=fields.Date.today) # Campo a generarse en la tabla _name
    

    usuarios_ids = fields.One2many('res.users','equipos_ids',string="Equipos")


    active = fields.Boolean(default=True)
   #Workflow
    state = fields.Selection([
           ('disponible', "Disponible"),
           ('asignado', "Asignado"),
           ('mantenimiento', "Mantenimiento"),
           ('baja', "Baja"),
    ], default='disponible')

    #Metodos para el Workflow
    @api.one
    def accion_disponible(self):
        self.state = 'disponible'

    @api.one
    def accion_asignado(self):
        self.state = 'asignado'

    @api.one
    def accion_mantenimiento(self):
        self.state = 'mantenimiento'

    @api.one
    def accion_baja(self):
        self.state = 'baja'
        self.active = False


        

class SistemaOperativo(models.Model):
    _name = 'equipment.software'

    name = fields.Char(readonly = True,compute="_get_full_software")
    swname =  fields.Char(string="Sistema Operativo", required=True, default="SO")
    version =  fields.Char(string="Version", required=True, default="1.0")
    
    @api.one
    @api.depends("swname", "version")
    def _get_full_software(self):
        self.name = str(self.swname) + " " +str(self.version)
        


class tipo(models.Model):
    _name = 'equipment.tipo'
    
    name = fields.Char(string="Tipo de Equipo", required=True)


class office(models.Model):
    _name = 'equipment.office'

    name = fields.Char(string="Nombre", required=True)
    version = fields.Char(required=True)


class procesador(models.Model):
    _name = 'equipment.procesador'

    name = fields.Char(string="Nombre", required=True)
    nucleo =  fields.Char(required=True)
