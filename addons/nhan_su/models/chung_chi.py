from odoo import models, fields


class ChungChi(models.Model):
    _name = 'chung_chi'
    _description = 'Chứng Chỉ'

    ma_chung_chi = fields.Char("Mã Chứng Chỉ", required=True)
    ten_chung_chi = fields.Char("Tên Chứng Chỉ", required=True)
    mo_ta = fields.Char("Mô Tả")

    nhan_vien_ids = fields.Many2many(comodel_name='nhan_vien', string="Nhân viên")
    nhan_vien_id = fields.Many2one(comodel_name='nhan_vien', string="Nhân viên", store=True)
