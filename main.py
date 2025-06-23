def main():
    while True:
        print("選択してください：")
        print("1: ライト@53期")
        print("2: やまちゃん@54期")
        print("3: やんこ")
        print("q: 終了")

        choice = input("> ")

        if choice == "1":
            print("１人目の変更です")
        elif choice == "2":
            print("2人目の変更です")
        elif choice == "3":
            print("3人目の変更です")
        elif choice == "q":
            print("プログラムを終了します。")
            break
        else:
            print("無効な入力です。もう一度選択してください。")

if __name__ == "__main__":
    main()
