# -*- coding: utf-8 -*-

{
    'name': 'LigaDrinks',
    'version': '0.1',
    'category': 'Point of Sale',
    'sequence': 6,
    'summary': 'Point os sale customization for LigaDrinks',
    'description': """
This module contains the customization for the LigaDrinks Business.
""",
    'depends': ['point_of_sale'],
    'data': [
        'views/liga_drinks_views.xml',
        'views/liga_drinks_templates.xml'
    ],
    'qweb': [
        'static/src/xml/pos.xml',
    ],
    'installable': True,
    'website': 'https://www.ligadrinks.com.br',
}
