import pywhatkit as kit

kit.sendwhatmsg("+62...", "Masukan text yang akan di kirim", 19, 7, wait_time=20, print_waitTime=True)

# nomor hp diubah sesuai tujuan dengan awalan menggunakan "+62" atau kode negara
# gunakan format waktu 24 JAM
# format tanggal nya yaitu menit jam dan menit, "19" adalah Jam, dan "7" adalah menit
# value wait_time bisa di sesuikan dengan kebutuhan, dalam satuan (detik)