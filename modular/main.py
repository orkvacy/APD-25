import necessaryFunction as nf


def main():
    while True:
        nf.load()
        mood = input('\nBagaimana Mood kalian hari ini?(ketik 0 jika ingin keluar) ')
        print(mood)
        nf.delayInput()
        nf.clear()
        if mood == '0':
            return False

if __name__ == "__main__":
    main()