from odoo import models, fields

class VanBanDen(models.Model):
    _name = 'van_ban_den'
    _description = 'Văn bản đến'

    ma = fields.Char('Mã', required=True)
    thoi_gian = fields.Datetime('Thời gian', default=fields.Datetime.now)
    nguoi_gui = fields.Char('Người gửi')
    ky_xac_nhan = fields.Char('Ký xác nhận')
    han = fields.Date('Hạn')
    file_dinh_kem = fields.Binary('File đính kèm')
