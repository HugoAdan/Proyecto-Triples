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
           'view/sesion_plataforma_view.xml',
           'view/equipo_computo_view.xml',
           'view/sucursales_view.xml',
           'view/depto_view.xml',
           'view/usuario_view.xml',
           #'view/historial_view.xml',
           'security/ir.model.access.csv'
         #'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/openacademy_course_demo.xml',
    ],
    'installable':True,
}