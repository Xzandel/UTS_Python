from minimarket import db

class Barang(db.Model):
   __tablename__ = 'tBarang'
   KodeBrg = db.Column(db.Integer(), primary_key=True)
   NamaBrg = db.Column(db.String(40), unique=True)
   Jenis = db.Column(db.String(25))
   Stok = db.Column(db.Integer())

   def __init__(self, KodeBrg, NamaBrg, Jenis, Stok):
      self.KodeBrg = KodeBrg
      self.NamaBrg = NamaBrg
      self.Jenis = Jenis
      self.Stok = Stok

   def __repr__(self):
      return '[%s, %s, %s, %s]' % \
         (self.KodeBrg, self.NamaBrg, self.Jenis, self.Stok)


