from odoo import models, fields, api
from datetime import time


class ChamCong(models.Model):
    _name = 'cham_cong'
    _description = 'Chấm công'

    nhan_vien_id = fields.Many2one(
        'nhan_vien', string='Nhân viên', required=True
    )

    ngay_cham_cong = fields.Date(
        string='Ngày chấm công', default=fields.Date.today
    )

    gio_vao = fields.Datetime("Giờ vào")
    gio_ra = fields.Datetime("Giờ ra")

    trang_thai = fields.Selection(
        [
            ('binh_thuong', 'Bình thường'),
            ('muon', 'Muộn'),
            ('vi_pham', 'Vi phạm'),
        ],
        string='Trạng thái',
        compute='_compute_trang_thai',
        store=True
    )

    @api.depends('gio_vao', 'gio_ra')
    def _compute_trang_thai(self):
        gio_chuan = time(8, 30)   # 08:30
        gio_ve = time(17, 30)     # 17:30

        for r in self:
            if not r.gio_vao or not r.gio_ra:
                r.trang_thai = False
                continue

            gio_vao_local = fields.Datetime.context_timestamp(
                r, r.gio_vao
            ).time()

            gio_ra_local = fields.Datetime.context_timestamp(
                r, r.gio_ra
            ).time()

            if gio_ra_local < gio_ve:
                r.trang_thai = 'vi_pham'
            elif gio_vao_local > gio_chuan:
                r.trang_thai = 'muon'
            else:
                r.trang_thai = 'binh_thuong'
