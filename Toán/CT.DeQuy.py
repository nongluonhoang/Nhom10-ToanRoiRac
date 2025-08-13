def to_hop_de_quy(n, k):
    """
    Hàm đệ quy tính tổ hợp C(n, k)
    """
    # Trường hợp cơ sở
    if k == 0 or k == n:
        return 1
    # Công thức đệ quy
    return to_hop_de_quy(n - 1, k - 1) + to_hop_de_quy(n - 1, k)

# Ví dụ sử dụng:
n = 5
k = 2
print(f"C({n}, {k}) = {to_hop_de_quy(n, k)}")




#VD:
#n=5
#k=2