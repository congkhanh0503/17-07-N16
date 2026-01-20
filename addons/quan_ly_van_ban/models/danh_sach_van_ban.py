from odoo import models, fields, api

class DanhSachVanBan(models.Model):
    _name = 'danh_sach_van_ban'
    _description = 'Danh sách văn bản'
    _rec_name = 'ten'

    ten = fields.Char('Tên văn bản', required=True)
    ma = fields.Char('Mã', required=True)
    
    # TRƯỜNG FILE: Thêm parameter filename để Odoo biết dùng trường nào làm tên file
    file_dinh_kem = fields.Binary('File đính kèm')
    file_name = fields.Char('Tên file') # Dùng để lưu tên file gốc (ví dụ: baocao.pdf)

    khach_hang_id = fields.Many2one('khach_hang', string="Khách hàng")
    loai_van_ban_id = fields.Many2one('loai_van_ban', string='Loại văn bản')
    nhan_vien_phu_trach_id = fields.Many2one('nhan_vien', string='Nhân viên phụ trách')
    thoi_gian = fields.Datetime('Thời gian', default=fields.Datetime.now)
    trang_thai = fields.Selection([
        ('draft', 'Nháp'),
        ('active', 'Hoạt động'),
        ('archived', 'Lưu trữ')
    ], string='Trạng thái', default='draft')

class KhachHangInherit(models.Model):
    _inherit = 'khach_hang'

    van_ban_ids = fields.One2many(
        'danh_sach_van_ban', 
        'khach_hang_id', 
        string="Hồ sơ văn bản"
    )