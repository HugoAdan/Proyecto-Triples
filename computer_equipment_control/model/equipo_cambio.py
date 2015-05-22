# -*- coding: utf-8 -*-
from openerp import api, exceptions, fields, models, _


"""
Este modulo crea el modelo Cambios
"""
#Se crea la clase Historial
class Cambios(models.Model):

    _name = 'equipment.cambios'


    equipo_id =  fields.Many2one("equipment.control",
                                    ondelete='cascade',
                                    string="Id Equipo", 
                                    index=True)
    tipo_id = fields.Many2one("equipment.tipo",
                                    ondelete='cascade',
                                    string="Tipo de Equipo",
                                    index=True, readonly=True)
    ram = fields.Float(digits=(3, 3),
    	               help="Especificación en GB",
    	               string="RAM", readonly=True)
    dd = fields.Float(digits=(3, 0), 
    	              help="Especificación de GB",
    	              string="Disco Duro", readonly=True)

    procesador_id = fields.Many2one("equipment.procesador",
                                    ondelete='cascade',
                                    string="Procesador",
                                    index=True, readonly=True)
    
    software_id = fields.Many2one("equipment.so",
                                    ondelete='cascade',
                                    string="Sistema Operativo",
                                    index=True, readonly=True)

    programas_id = fields.Many2many("equipment.programas",
                                    ondelete='cascade',
                                    string="Programas",
                                    index=True, readonly=True)


    responsible_id = fields.Many2one("res.users",
                                    ondelete='set null',
                                    string="Responsable del Equipo",
                                    index=True, readonly=True)
    
#Factura - Habilitar)
    folio = fields.Char(string="Folio",
                        readonly=True) # Campo a generarse en la tabla _name
    provider = fields.Char(string="Proveedor",
                           readonly=True) # Campo a generarse en la tabla _name
    date = fields.Date(string="Fecha",
                       default=fields.Date.today,
                       readonly=True) # Campo a generarse en la tabla _name
    active = fields.Boolean(default=True, readonly=True)
   #Workflow
    state = fields.Selection([
           ('disponible', "Disponible"),
           ('asignado', "Asignado"),
           ('mantenimiento', "Mantenimiento"),
           ('baja', "Baja"),
    ], default='disponible')


#    name = fields.Char(readonly = True, compute="_get_full_historial")
#
#    @api.one
#    def _get_full_historial(self):
#        self.name = "Equipo " +str(self.equipo_id.id)

