from odoo import models, fields, api


class NhanVien(models.Model):
    _name = 'nhan_vien'
    _description = 'Bảng chứa thông tin nhân viên'
    _rec_name = 'ten_nv'
    
    ma_dinh_danh = fields.Char("Mã định danh", required=True)
    ten_nv = fields.Char("Tên nhân viên", required=True)
    ngay_sinh = fields.Date("Ngày sinh")
    que_quan = fields.Char("Quê quán")
    email = fields.Char("Email")
    so_dien_thoai = fields.Char("Số điện thoại")
    cccd = fields.Char("CCCD", required=True)
    ma_so_bhxh = fields.Char("Mã số BHXH", required=True)
    luong = fields.Float("Lương")

    phong_ban_ids = fields.Many2many(
        comodel_name='phong_ban',
        string="Phòng ban"
    )

    chung_chi_ids = fields.One2many(
        comodel_name='chung_chi',
        inverse_name="nhan_vien_id",
        string="Chứng chỉ"
    )
    hop_dong_ids = fields.One2many(
        comodel_name='hop_dong',
        inverse_name='nhan_vien_id',
        string='Hợp đồng lao động'
    )
    cham_cong_ids = fields.One2many(
    comodel_name='cham_cong',
    inverse_name='nhan_vien_id',
    string='Chấm công'
    )
    bang_luong_ids = fields.One2many(
        'bang_luong', 'nhan_vien_id', string='Bảng lương'
    )
    phong_ban_id = fields.Many2one(
    'phong_ban',
    string='Phòng ban',
    required=True
    )