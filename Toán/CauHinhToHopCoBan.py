import math

def to_hop(n, k):
    """
    Hàm tính tổ hợp chập k của n (C(n, k))
    """
    if k < 0 or k > n:
        return 0
    return math.comb(n, k)  # Python 3.8+ có sẵn hàm này

# Ví dụ sử dụng:
n = 5
k = 2
print(f"C({n}, {k}) = {to_hop(n, k)}")


#VD:
#n=5
#k=2