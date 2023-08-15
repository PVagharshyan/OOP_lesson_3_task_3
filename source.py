import obj

COUNT = 10

def main() -> None:
    list_obj = [obj.obj() for i in range(COUNT)]
    for i in range(COUNT):
        print(f"I am object number {list_obj[i].get_serial_number}.")

if __name__ == "__main__":
    main()
