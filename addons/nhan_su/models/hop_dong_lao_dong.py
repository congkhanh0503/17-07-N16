from odoo import models, fields

class HopDongLaoDong(models.Model):
    _name = 'hop_dong'
    _description = 'Hợp đồng lao động'

    name = fields.Char(
        string='Số hợp đồng',
        required=True
    )

    nhan_vien_id = fields.Many2one(
        comodel_name='nhan_vien',
        string='Nhân viên',
        required=True,
        ondelete='cascade'
    )

    ngay_bat_dau = fields.Date(
        string='Ngày bắt đầu',
        required=True
    )

    ngay_ket_thuc = fields.Date(
        string='Ngày kết thúc'
    )

    luong = fields.Float(
        string='Lương cơ bản'
    )

    trang_thai = fields.Selection(
        [
            ('nhap', 'Nháp'),
            ('hieu_luc', 'Có hiệu lực'),
            ('het_han', 'Hết hạn'),
        ],
        string='Trạng thái',
        default='nhap'
    )
