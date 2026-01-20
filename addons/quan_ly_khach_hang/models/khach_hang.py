from odoo import fields, models, api

class KhachHang(models.Model):
    _name = 'khach_hang'
    _description = 'Khách Hàng'
    _rec_name = 'full_name'

    # 1. Chuyển thành trường Char bình thường để người dùng tự nhập
    full_name = fields.Char(string='Họ và tên', required=True)
    
    email = fields.Char(string='Email', required=True)
    phone = fields.Char(string='Số điện thoại', required=True)
    address = fields.Char(string='Địa chỉ')
    birthday = fields.Date(string='Ngày sinh')

    # Liên kết dữ liệu
    hop_dong_ids = fields.One2many('hop_dong', 'khach_hang_id', string="Danh sách hợp đồng")
    ho_tro_ids = fields.One2many('ho_tro_khach_hang', 'khach_hang_id', string='Hỗ trợ khách hàng')
    khach_hang_tiem_nang_ids = fields.One2many('khach_hang_tiem_nang', 'khach_hang_id', string='Khách hàng tiềm năng')

    # 2. XÓA hàm _compute_full_name vì không còn dùng đến nữa