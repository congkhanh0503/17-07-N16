from odoo import models, fields


class TaiSan(models.Model):
    _name = 'tai_san'
    _description = 'Tài Sản'

    ma_tai_san = fields.Char("Mã Tài Sản", required=True)
    ten_tai_san = fields.Char("Tên Tài Sản", required=True)
    mo_ta = fields.Char("Mô Tả")

