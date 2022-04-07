from minimarket import db

class BarangMasuk(db.Model):
    __tablename__ = 'tBarangMasuk'
    KodeBrgIn = db.Column(db.Integer(), primary_key=True)
    KodeBrg = db.Column(db.Integer())
    TglMasuk = db.Column(db.Date())
    Jumlah = db.Column(db.Integer())
    Supplier = db.Column(db.String(30))

    def __init__(self, **kwargs):
        self.KodeBrgIn = kwargs['KodeBrgIn']
        self.KodeBrg = kwargs['KodeBrg']
        self.TglMasuk = kwargs['TglMasuk']
        self.Jumlah = kwargs['Jumlah']
        self.Supplier = kwargs['Supplier']

    def __repr__(self):
        return'[%s, %s, %s, %s, %s]' % \
              (self.KodeBrgIn, self.KodeBrg, self.TglMasuk, self.Jumlah, self.Supplier)
