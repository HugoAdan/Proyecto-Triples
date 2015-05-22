# -*- coding: utf-8 -*-
from openerp import api, exceptions, fields, models, _

"""
Este modulo crea el modelo Control
"""
#Se crea la clase Control
class Control(models.Model):
    
    _name = 'equipment.control' # String crea entidad tomado por odoo 
                                 #para crear tabla en postgres

    name = fields.Char(readonly = True, compute="_get_full_historial", string="ID")

    tipo_id = fields.Many2one('equipment.tipo',
                                    ondelete='set null',string="Tipo de Equipo", index=True)

    ram = fields.Float(digits=(3, 3), help="Especificación en GB", string="RAM", required=True)
    dd = fields.Float(digits=(3, 0), help="Especificación de GB", string="Disco Duro", required=True)

    procesador_id = fields.Many2one("equipment.procesador",
                                    ondelete='set null',string="Procesador", index=True)
    
    software_id = fields.Many2one("equipment.so",
                                    ondelete='set null',string="Sistema Operativo", index=True)

    programas_id = fields.Many2many("equipment.programas",
                                    ondelete='set null',string="Programas", index=True)


    responsible_id = fields.Many2one("res.users",
                                    ondelete='set null',string="Responsable del Equipo", index=True)  
    
#Factura - Habilitar)
    folio = fields.Char(string="Folio") # Campo a generarse en la tabla _name
    provider = fields.Char(string="Proveedor") # Campo a generarse en la tabla _name
    date = fields.Date(string="Fecha", default=fields.Date.today) # Campo a generarse en la tabla _name

    active = fields.Boolean(default=True)
   #Workflow
    state = fields.Selection([
           ('disponible', "Disponible"),
           ('asignado', "Asignado"),
           ('mantenimiento', "Mantenimiento"),
           ('baja', "Baja"),
    ], default='disponible', string="Estado del equipo")

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


    @api.one
    def write(self, vals):
        print "**************************************"
        equipo_cambio_obj = self.env['equipment.cambios']
        #import pdb; pdb.set_trace()
        print vals
        diccionario = {
           'equipo_id': self.id or False,
           'tipo_id': vals.get('tipo_id') or False,
           'ram': vals.get('ram') or False,
           'dd': vals.get('dd') or False,
           'procesador_id': vals.get('procesador_id') or False,
           'software_id': vals.get('software_id') or False,
           'programas_id': vals.get('programas_id') or False,
           'responsible_id': vals.get('responsible_id') or False,
           }
        equipo_cambio_obj.create(diccionario)
        #print self.ram, self.dd
        return super(Control, self).write(vals)

    @api.model
    def create(self, vals):
        print "Create**************************************"
        equipo_cambio_obj = self.env['equipment.cambios']
        #import pdb; pdb.set_trace()
        print "create", vals
        re = super(Control, self).create(vals)
        diccionario = {
           'equipo_id': re.id or vals.get('id') or False,
           'tipo_id': vals.get('tipo_id') or False,
           'ram': vals.get('ram') or False,
           'dd': vals.get('dd') or False,
           'procesador_id': vals.get('procesador_id') or False,
           'software_id': vals.get('software_id') or False,
           'programas_id': vals.get('programas_id') or False,
           'responsible_id': vals.get('responsible_id') or False,
           }
        equipo_cambio_obj.create(diccionario)
        #print self.ram, self.dd
        print re
        return re






    


    @api.one
    def _get_full_historial(self):
        self.name = "Equipo " +str(self.id)




       

class SistemaOperativo(models.Model):
    _name = 'equipment.so'

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


class programas(models.Model):
    _name = 'equipment.programas'

    name = fields.Char(readonly = True,compute="_get_full_programa")
    program_name =  fields.Char(string="Nombre", required=True, default="Programa")
    version = fields.Char(string="Version", required=True, default="Version")
    licencia = fields.Char(string="Licencia", default="")
    descripcion = fields.Char(string="Descripcion", default="")
    
    
 
    @api.one
    @api.depends("program_name", "version")
    def _get_full_programa(self):
        self.name = str(self.program_name) + " " +str(self.version)




class procesador(models.Model):
    _name = 'equipment.procesador'

    name = fields.Char(readonly = True,compute="_get_full_procesador")
    procesadorname =  fields.Char(string="Procesador", required=True, default="Procesador")
    nucleo =  fields.Char(required=True, default="Nucleo")

    @api.one
    @api.depends("procesadorname", "nucleo")
    def _get_full_procesador(self):
        self.name = str(self.procesadorname) + " " +str(self.nucleo)

