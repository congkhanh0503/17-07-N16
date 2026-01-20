from odoo import models, fields

class VanBanNoiBo(models.Model):
    _name = 'van_ban_noi_bo'
    _description = 'Văn bản nội bộ'

    ma = fields.Char('Mã', required=True)
    thoi_gian = fields.Datetime('Thời gian', default=fields.Datetime.now)
    nguoi_gui = fields.Many2one('nhan_vien', string='Người gửi')
    nguoi_nhan = fields.Many2one('nhan_vien', string='Người nhận')
    mo_ta = fields.Text('Mô tả')
    file_dinh_kem = fields.Binary('File đính kèm')
