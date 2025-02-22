while(True):
    n = int(input())
    if n == -1:
        break

    sum = 0
    div = []
    for i in range(1, n):
        if n % i == 0:
            div.append(str(i))
            sum+=i

    if sum == n:
        print(str(n)+" = "+" + ".join(div))

    else:
        print(str(n)+" is NOT perfect.")