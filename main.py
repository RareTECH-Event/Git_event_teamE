def main():
    while True:
        print("選択してください：")
        print("1: ゆきんこ@52期")
        print("2: ライト@53期")
        print("3: しーさん＠53期")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("頑張りましょう！！！")
        elif choice == "2":
            print("ちょっと感動！")
        elif choice == "3":
            print("皆さんありがとう")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()

