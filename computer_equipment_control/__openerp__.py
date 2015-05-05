# -*- coding: utf-8 -*-
{
    'name': "Computer Equipment Control",

    'summary': """Equipment Controls""",

    'description':"""
        Control de Equipos de Cómputo
               -Permisos
               -Dispositivos y Equipos de Computo
               -Sucursales
               -Departamentos
               -Usuarios
               -Graficos Estadisticos
               -Historial

    """,

    'author': "Andrea Magdalena Rocio Gutierrez",
    'website': "andyrociogtz@gmail.com",

    'category': 'Generic Modules',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',],

    # always loaded
    'data': [            
           'view/usuario_view.xml',
           'view/equipo_computo_view.xml',
           'view/equipo_cambios_view.xml',
           'view/sucursales_view.xml',
           'view/depto_view.xml',
           'workflow/equipo_workflow_view.xml',
           'security/ir.model.access.csv'
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/openacademy_course_demo.xml',
    ],
    'installable':True,
}