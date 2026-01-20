from odoo import _, api, fields, models

class KhachHangTiemNang(models.Model):
    _name = 'khach_hang_tiem_nang'
    _description = 'Khách hàng tiềm năng'
    _rec_name = 'ten_cong_ty'
    
    ten_cong_ty = fields.Char(string='Tên công ty', required=True)
    giai_doan = fields.Selection([
        ('1', 'Tiếp cận'),
        ('2', 'Đàm phán'),
        ('3', 'Ký hợp đồng'),
        ('4', 'Thất bại'),
    ], string='Giai đoạn', required=True, default='1')
    
    doanh_thu_tiem_nang = fields.Float(string='Doanh thu tiềm năng')
    ngay_du_kien_ky_hop_dong = fields.Date(string='Ngày dự kiến ký hợp đồng')
    ngay_tao = fields.Date(string='Ngày tạo', default=fields.Date.today, readonly=True)
    ngay_cap_nhat = fields.Date(string='Ngày cập nhật', default=fields.Date.today, readonly=True)

    # CHỌN KHÁCH HÀNG TỪ DANH SÁCH KHÁCH HÀNG (Khách hàng gốc)
    khach_hang_id = fields.Many2one('khach_hang', string='Khách hàng liên kết')

    # LIÊN KẾT DỮ LIỆU
    # Chỉ giữ lại 'hoat_dong_ids' nếu model 'hoat_dong' có trường 'khach_hang_tiem_nang_id'
    hoat_dong_ids = fields.One2many('hoat_dong', 'khach_hang_tiem_nang_id', string='Hoạt động')
    

    @api.model
    def create(self, vals):
        return super(KhachHangTiemNang, self).create(vals)

    def write(self, vals):
        vals['ngay_cap_nhat'] = fields.Date.today()
        return super(KhachHangTiemNang, self).write(vals)