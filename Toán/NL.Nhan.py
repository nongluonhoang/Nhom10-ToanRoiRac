def tich_so_cach(*so_cach_cac_buoc):
    """
    Hàm tính tích số cách qua nhiều bước (nguyên lý nhân)
    Tham số: truyền vào số cách của từng bước
    """
    tich = 1
    for so_cach in so_cach_cac_buoc:
        tich *= so_cach
    return tich

# Ví dụ sử dụng:
mon_chinh = 3
do_uong = 2
trang_mieng = 4

tong_cach = tich_so_cach(mon_chinh, do_uong, trang_mieng)
print(f"Tổng số cách lựa chọn: {tong_cach}")




#VD:
#Chọn món chính: 3 cách
#Chọn đồ uống: 2 cách
#Chọn tráng miệng: 4 cách
#Tổng số cách chọn = 
#3×2×4=24
#3×2×4=24 cách.