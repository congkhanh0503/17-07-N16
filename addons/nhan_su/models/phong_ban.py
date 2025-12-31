from odoo import models, fields


class PhongBan(models.Model):
    _name = 'phong_ban'
    _description = 'Phòng ban'

    ma_phong = fields.Char("Mã phòng", required=True)
    ten_phong = fields.Char("Tên phòng", required=True)

    nhan_vien_ids = fields.One2many(
        'nhan_vien',
        'phong_ban_id',
        string='Danh sách nhân viên'
    )

    def name_get(self):
        res = []
        for r in self:
            name = f"[{r.ma_phong}] {r.ten_phong}"
            res.append((r.id, name))
        return res
