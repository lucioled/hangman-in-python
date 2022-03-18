if __name__ == '__main__':
    my_list = [i for i in range(1, 99999) if i %
               4 == 0 if i % 6 == 0 if i % 9 == 0]

    print(my_list)
