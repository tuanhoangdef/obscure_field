# -*- coding: utf-8 -*-
{
    'name': 'Obscure Field',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Store sensitive character fields without exposing values in RPC/read/export responses',
    'description': 'Add fields.Obscure for sensitive credentials that should be masked in Odoo read, web_read, and export payloads.',
    'author': 'tuanhoangdef <hng.atuan@gmail.com>',
    'license': 'LGPL-3',
    'price': 0,
    'currency': 'USD',
    'depends': ['base', 'web'],
    'data': [],
    'images': [
        'static/description/icon.png',
    ],
    'website': 'https://github.com/tuanhoangdef/obscure_field/tree/19.0/',
    'installable': True,
    'application': False,
    'auto_install': False,
}
