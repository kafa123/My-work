nama_barang=input("nama barang =",)
print("ketik 1 untuk mencari harga jual")
print("ketik 2 untuk mencari harga beli")
print("ketik 3 untuk mencari banyak barang")
print("ketik 4 untuk mencari keuntungan")
x=int(input())
if x == 1:
    keuntungan=input("keuntungan yang ingin diperoleh = ",)
    keuntungan=int(keuntungan)

    banyak_barang=input("banyak barang = ",)
    banyak_barang=int(banyak_barang)

    harga_beli=input("harga beli per pcs = ",)
    harga_beli=int(harga_beli)

    #keuntungan=banyak barang  x harga jual -banyak barang x  harga beli
    #keuntungan/banyak barang=harga jual - harga beli
    harga_jual=keuntungan/banyak_barang + harga_beli
    harga_jual="{:.0f}".format(harga_jual)
    harga_jual=str(harga_jual)
    harga_jual="anda harus menjual "+(nama_barang)+" tersebut dengan harga Rp."+harga_jual
    print(harga_jual)


elif x== 2:
    keuntungan=input("keuntungan yang ingin diperoleh = ",)
    keuntungan=int(keuntungan)

    banyak_barang=input("banyak barang = ",)
    banyak_barang=int(banyak_barang)

    harga_jual=input("harga jual per pcs = ",)
    harga_jual=int(harga_jual)

    #keuntungan=banyak barang  x harga jual -banyak barang x  harga beli
    #keuntungan/banyak barang=harga jual - harga beli
    harga_beli=harga_jual-keuntungan/banyak_barang
    harga_beli="{:.0f}".format(harga_beli)
    harga_beli=str(harga_beli)
    harga_beli="anda harus membeli/membuat "+ nama_barang +" tersebut seharga Rp."+harga_beli
    print(harga_beli)

elif x==3:
    keuntungan=input("keuntungan yang ingin diperoleh = ",)
    keuntungan=int(keuntungan)

    harga_beli=input("harga beli per pcs = ",)
    harga_beli=int(harga_beli)

    harga_jual=input("harga jual per pcs = ",)
    harga_jual=int(harga_jual)

    #keuntungan=banyak barang  x harga jual -banyak barang x  harga beli
    #keuntungan/banyak barang=harga jual - harga beli
    banyak_barang=keuntungan/(harga_jual - harga_beli)
    banyak_barang="{:.0f}".format(banyak_barang)
    banyak_barang=str(banyak_barang)
    keuntungan=str(keuntungan)
    harga_beli=str(harga_beli)
    harga_jual=str(harga_jual)
    banyak_barang="jika anda ingin mendapatkan keuntungan sebesar Rp."+keuntungan+" dengan harga jual sebesar Rp." +harga_jual+" dan harga beli sebesar Rp."+harga_beli+" maka anda harus menjualnya sebanyak "+ banyak_barang+ " buah"
    print(banyak_barang)

elif x==4:
    harga_jual=input("harga jual per pcs =",)
    harga_jual=int(harga_jual)

    banyak_barang=input("banyak barang = ",)
    banyak_barang=int(banyak_barang)

    harga_beli=input("harga beli per pcs = ",)
    harga_beli=int(harga_beli)

    keuntungan=harga_jual*banyak_barang-harga_beli*banyak_barang
    keuntungan="{:.0f}".format(keuntungan)
    banyak_barang=str(banyak_barang)
    keuntungan=str(keuntungan)
    harga_beli=str(harga_beli)
    harga_jual=str(harga_jual)
    keuntungan="dengan menjual "+nama_barang+" sebesar Rp."+harga_jual+" dan harga beli sebesar Rp."+harga_beli+" serta memiliki barang sebanyak "+banyak_barang+" maka keuntungan yang anda peroleh adalah Rp."+keuntungan
    print(keuntungan)
else :
    print("mohon pilih angka 1-4")

