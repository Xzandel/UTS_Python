from minimarket import db

class BarangOut(db.Model):
    __tablename__ = 'tBarangKeluar'
    KodeBrgOut = db.Column(db.Integer(), primary_key=True)
    KodeBrg = db.Column(db.Integer())
    TglKeluar = db.Column(db.Date())
    Jumlah = db.Column(db.Integer())

    def __init__(self, **kwargs):
        self.KodeBrgOut = kwargs['KodeBrgOut']
        self.KodeBrg = kwargs['KodeBrg']
        self.TglKeluar = kwargs['TglKeluar']
        self.Jumlah = kwargs['Jumlah']

    def __repr__(self):
        return'[%s, %s, %s, %s]' % \
              (self.KodeBrgOut, self.KodeBrg, self.TglKeluar, self.Jumlah)