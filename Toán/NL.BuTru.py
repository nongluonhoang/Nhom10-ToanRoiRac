#Hàm nguyên lý bù trừ cho 2 tập hợp

def bu_tru_2(a, b, ab):
    """
    Nguyên lý bù trừ cho 2 tập hợp:
    a: |A|
    b: |B|
    ab: |A ∩ B|
    """
    return a + b - ab



#Hàm chuyên lý bù trừ cho 3 tập hợp

def bu_tru_3(a, b, c, ab, ac, bc, abc):
    """
    Nguyên lý bù trừ cho 3 tập hợp:
    a: |A|, b: |B|, c: |C|
    ab: |A ∩ B|, ac: |A ∩ C|, bc: |B ∩ C|
    abc: |A ∩ B ∩ C|
    """
    return a + b + c - ab - ac - bc + abc



#Lọc số không chia hết cho tập số trước
#VD:lọc các số từ 1 đến 100 không chia hết cho 2, 3 hoặc 5

def loc_khong_chia_het(N, tap_so):
    """
    Lọc các số từ 1..N không chia hết cho bất kỳ số nào trong tap_so
    """
    ket_qua = []
    for x in range(1, N + 1):
        if all(x % p != 0 for p in tap_so):
            ket_qua.append(x)
    return ket_qua

# Ví dụ:
N = 30
tap_so = [2, 3, 5]
ds = loc_khong_chia_het(N, tap_so)
print(f"Các số từ 1 đến {N} không chia hết cho {tap_so}:")
print(ds)
print(f"Số lượng: {len(ds)}")
