import re
from odoo import fields as odoo_fields
from odoo.tools.misc import SENTINEL


class Obscure(odoo_fields.Char):
    """Char-compatible field that hides its value in ORM read payloads.

    The real value remains available to server-side Python code through
    ``record.field_name``. RPC/read/export responses only receive the placeholder.
    This is intentionally not encryption; it only prevents browser/network leaks.
    """

    type = 'char'
    obscure = True
    obscure_placeholder = '******'

    def __init__(self, string=SENTINEL, **kwargs):
        kwargs.setdefault('copy', False)
        kwargs.setdefault('exportable', False)
        super().__init__(string=string, **kwargs)

    def _obscure_value(self, value):
        return self.obscure_placeholder if value else False

    def _is_obscured_value(self, value):
        obscured_value_re = re.compile(r'^\*+$')
        return isinstance(value, str) and bool(obscured_value_re.fullmatch(value))

    def write(self, records, value):
        if self._is_obscured_value(value):
            return
        return super().write(records, value)

    def convert_to_read(self, value, record, use_display_name=True):
        return self._obscure_value(value)

    def convert_to_export(self, value, record):
        return self._obscure_value(value) or ''

    _description_obscure = property(lambda self: self.obscure)


odoo_fields.Obscure = Obscure
