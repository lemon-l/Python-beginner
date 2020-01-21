def search(x):
    return{'q': 'a', 'w': 'b', 'e': 'c', 'r': 'd', 't': 'e', 'y': 'f', 'u': 'g', 'i': 'h', 'o': 'i', 'p': 'j', 'a': 'k',
           's': 'l', 'd': 'm', 'f': 'n', 'g': 'o', 'h': 'p', 'j': 'q', 'k': 'r',
           'l': 's', 'z': 't', 'x': 'u', 'c': 'v', 'v': 'w', 'b': 'x', 'n': 'y', 'm': 'z',
           }.get(x, x)


def main():
    print("QWE键盘解密程序")
    print("请输入待解密的字符串：")
    while True:
        try:
            miwen = input()
            miwen = miwen.lower()
            print("结果是：")
            for i in miwen:
                print(search(i), end='')
            print("\n")
        except:
            break


if __name__ == "__main__":
    main()
