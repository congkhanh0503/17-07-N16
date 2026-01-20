from odoo import models, fields

class VanBanDi(models.Model):
    _name = 'van_ban_di'
    _description = 'Văn bản đi'

    ma = fields.Char('Mã', required=True)
    thoi_gian = fields.Datetime('Thời gian', default=fields.Datetime.now)
    nguoi_nhan = fields.Char('Người nhận')
    hinh_thuc = fields.Selection([
        ('email', 'Email'),
        ('fax', 'Fax'),
        ('ban_hanh', 'Bản hành chính')
    ], string='Hình thức')
    trang_thai = fields.Selection([
        ('cho_gui', 'Chờ gửi'),
        ('da_gui', 'Đã gửi')
    ], string='Trạng thái', default='cho_gui')
    file_dinh_kem = fields.Binary('File đính kèm')
