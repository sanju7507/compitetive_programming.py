import sys

def find_triplets():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    N = int(input_data[0])
    arr = [int(x) for x in input_data[1:N+1]]
    X = int(input_data[N+1])
    
    arr.sort()
    
    triplets_found = False
    
    for i in range(N - 2):
      
        if i > 0 and arr[i] == arr[i - 1]:
            continue
            
        left = i + 1
        right = N - 1
        
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            
            if current_sum == X:
                print(f"{arr[i]} {arr[left]} {arr[right]}")
                triplets_found = True
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left - 1]:
                    left += 1
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1
                    
            elif current_sum < X:
                left += 1
            else:
                right -= 1
                
    if not triplets_found:
        print("No Triplet Found")

if __name__ == '__main__':
    find_triplets()
