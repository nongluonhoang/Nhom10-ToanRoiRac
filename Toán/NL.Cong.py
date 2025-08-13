def tong_so_cach(*so_cach_cac_truong_hop):

    """
    Hàm tính tổng số cách khi các trường hợp rời nhau (nguyên lý cộng)
    Tham số: truyền vào số cách của từng trường hợp
    """

    return sum(so_cach_cac_truong_hop)


# Ví dụ sử dụng:
mon_chinh = 3
mon_trang_mieng = 4


tong_cach = tong_so_cach(mon_chinh, mon_trang_mieng)
print(f"Tổng số cách lựa chọn: {tong_cach}")



#VD
#Có 3 cách chọn món ăn chính
#Có 4 cách chọn món tráng miệng
#Nhưng khách chỉ chọn món chính hoặc món tráng miệng, không chọn cả hai.
#Hỏi: Có bao nhiêu cách chọn?