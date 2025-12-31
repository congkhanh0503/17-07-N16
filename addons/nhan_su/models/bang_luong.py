from odoo import models, fields, api
from datetime import date
import calendar


class BangLuong(models.Model):
    _name = 'bang_luong'
    _description = 'Bảng lương theo tháng'

    nhan_vien_id = fields.Many2one(
        'nhan_vien', string='Nhân viên', required=True
    )

    thang = fields.Integer("Tháng", required=True)
    nam = fields.Integer("Năm", required=True)

    luong_co_ban = fields.Float(
        string="Lương cơ bản",
        related="nhan_vien_id.luong",
        store=True,
        readonly=True
    )

    so_ngay_cong = fields.Float(
        "Số ngày công", compute='_compute_luong', store=True
    )

    phat = fields.Float(
        "Tiền phạt", compute='_compute_luong', store=True
    )

    luong_thuc_nhan = fields.Float(
        "Lương thực nhận", compute='_compute_luong', store=True
    )

    @api.depends(
        'nhan_vien_id',
        'thang',
        'nam',
        'nhan_vien_id.cham_cong_ids.trang_thai',
        'nhan_vien_id.cham_cong_ids.ngay_cham_cong'
    )
    def _compute_luong(self):
        ChamCong = self.env['cham_cong']

        for r in self:
            r.so_ngay_cong = 0
            r.phat = 0
            r.luong_thuc_nhan = 0

            if not r.nhan_vien_id or not r.thang or not r.nam:
                continue

            first_day = date(r.nam, r.thang, 1)
            last_day = date(
                r.nam,
                r.thang,
                calendar.monthrange(r.nam, r.thang)[1]
            )

            cham_cong = ChamCong.search([
                ('nhan_vien_id', '=', r.nhan_vien_id.id),
                ('ngay_cham_cong', '>=', first_day),
                ('ngay_cham_cong', '<=', last_day),
            ])

            cong = 0
            phat = 0

            for cc in cham_cong:
                if cc.trang_thai == 'binh_thuong':
                    cong += 1
                elif cc.trang_thai == 'muon':
                    cong += 1
                    phat += 50000
                elif cc.trang_thai == 'vi_pham':
                    cong += 0.5
                    phat += 100000

            luong_1_ngay = (r.luong_co_ban or 0) / 26
            r.so_ngay_cong = cong
            r.phat = phat
            r.luong_thuc_nhan = max(cong * luong_1_ngay - phat, 0)
