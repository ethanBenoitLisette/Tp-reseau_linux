import time

def count_to_10():
    for i in range(1, 11):
        print(i)
        time.sleep(0.5)

def main():
    count_to_10()
    count_to_10()

if __name__ == "__main__":
    main()
