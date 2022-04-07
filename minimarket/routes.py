from flask import Flask, render_template,\
   request,redirect,url_for, flash
from minimarket import application,db

from minimarket.models import barang as unit
from minimarket.models import barangin as unitin

@application.route('/')
def index():
   return render_template('index.html', container=unit.Barang.query.all(), container2=unitin.BarangMasuk.query.all())


@application.route('/tambahBarang', methods=['GET','POST'])
def tambahDataBarang():
   if request.method=='POST':
      KodeBrg = request.form['kode_barang']
      NamaBrg = request.form['txt_nama_barang']
      Jenis = request.form['txt_jenis']
      Stok = request.form['num_stok']
      Barang = unit.Barang(KodeBrg, NamaBrg, Jenis, Stok)
      db.session.add(Barang)
      db.session.commit()
      return redirect(url_for('index'))
   else:
      return render_template('createDataBarang.html')


@application.route('/ubahDataBarang/<KodeBrg>',methods=['GET','POST'])
def ubahDataBarang(KodeBrg):
   Units = unit.Barang.query.filter_by(KodeBrg=KodeBrg).first()
   if request.method=='POST':
      Units.KodeBrg = request.form['numKode']
      Units.NamaBrg = request.form['txtNamaBarang']
      Units.Jenis = request.form['txtJenis']
      Units.Stok = request.form['numStok']
      db.session.add(Units)
      db.session.commit()
      return redirect(url_for('index'))
   else:
      return render_template('ubahDataBarang.html',Units=Units)

@application.route('/hapusDataBarang/<KodeBrg>',methods=['GET','POST'])
def hapusDataBarang(KodeBrg):
   Units = unit.Barang.query.filter_by(KodeBrg=KodeBrg).first()
   db.session.delete(Units)
   db.session.commit()
   return redirect(url_for('index'))

@application.route('/tambahDataBarangIn',methods=['GET','POST'])
def tambahDataBarangIn():

   if request.method=='POST':
      KodeBrgIn = request.form['kode_barang_in']
      KodeBrg = request.form['kode_barang']
      TglMasuk = request.form['tgl_masuk']
      Jumlah = request.form['num_stok']
      Supplier = request.form['supplier']

      BarangIn = unitin.BarangMasuk(KodeBrgIn=KodeBrgIn, KodeBrg=KodeBrg, TglMasuk=TglMasuk, Jumlah=Jumlah, Supplier=Supplier)
      Unit = unit.Barang.query.filter_by(KodeBrg=KodeBrg).first()
      Unit.Stok = Unit.Stok + int(Jumlah)

      db.session.add(BarangIn)
      db.session.commit()
      db.session.add(Unit)
      db.session.commit()

      return redirect(url_for('index'))
   else:
      return render_template('createDataBarangIn.html')

@application.route('/ubahDataBarangIn/<KodeBrgIn>',methods=['GET','POST'])
def ubahDataBarangIn(KodeBrgIn):
   UnitsIn = unitin.BarangMasuk.query.filter_by(KodeBrgIn=KodeBrgIn).first()
   print(UnitsIn)
   if request.method=='POST':
      UnitsIn.KodeBrgIn = request.form['numKodeBrgIn']
      UnitsIn.KodeBrg = request.form['numKodeBrg']
      UnitsIn.TglMasuk = request.form['tanggalMasuk']
      UnitsIn.Jumlah = request.form['numJumlah']
      UnitsIn.Supplier = request.form['txtSupplier']
      Unit = unit.Barang.query.filter_by(KodeBrg=UnitsIn.KodeBrg).first()
      Unit.Stok = Unit.Stok + int(UnitsIn.Jumlah)
      print(UnitsIn)
      db.session.add(UnitsIn)
      db.session.commit()
      db.session.add(Unit)
      db.session.commit()
      return redirect(url_for('index'))
   else:
      return render_template('ubahDataBarangIn.html',UnitsIn=UnitsIn)

@application.route('/hapusDataBarangIn/<KodeBrgIn>',methods=['GET','POST'])
def hapusDataBarangIn(KodeBrgIn):
   Units = unitin.BarangMasuk.query.filter_by(KodeBrgIn=KodeBrgIn).first()
   db.session.delete(Units)
   db.session.commit()
   return redirect(url_for('index'))