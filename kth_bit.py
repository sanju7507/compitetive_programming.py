def is_kth_bit_set(n, k):
    if (n & (1 << k)) != 0:
        return 1
    else:
        return 0

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        k = int(input_data[1])
        print(is_kth_bit_set(n, k))
