def read():
    nmbr_list = []
    with open("./files/numbers.txt", "r") as file:
        for item in file:
            nmbr_list.append(int(item))
    return nmbr_list


def write():
    names = ["Lucio", "María", "Putin", "Biden"]
    with open("./files/names.txt", "w") as file:
        for name in names:
            file.write(name)
            file.write("\n")


def run():
    print(read())
    write()


if __name__ == "__main__":
    run()
