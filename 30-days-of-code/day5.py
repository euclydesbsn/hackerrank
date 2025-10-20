def tabuada(x):
    for i in range(1, 11):
        print(f"{x} x {i} = {x*i}")
  
if __name__ == '__main__':
    n = int(input().strip())
    tabuada(n)