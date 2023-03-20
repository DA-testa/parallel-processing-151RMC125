# python3


def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    thread_list = [0] * n
    for i in range(m):
        free_thread = min(thread_list)
        new_worker = thread_list.index(free_thread)
        start_time = thread_list[new_worker]
        output.append([new_worker, start_time])
        job_time = data[i]
        thread_list[new_worker] += job_time

    return output


def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    input_method = list(map(int, input().split()))
    n = input_method[0]
    m = input_method[1]

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n, m, data)
    
    # TODO: print out the results, each pair in it's own line
    for i, t in result:
        print(i, t)


if __name__ == "__main__":
    main()
