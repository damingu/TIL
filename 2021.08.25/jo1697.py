N = int(input())
queue = []

for i in range(N):
    order = input()
    # queue push
    if order[0] == 'i':
        queue.append(order[2:])
    # queue pop
    elif order[0] == 'o':
        if len(queue) == 0 :
            print("empty")
        else:
            print(queue.pop(0))
    # queue length
    elif order[0] == 'c':
        print(len(queue))