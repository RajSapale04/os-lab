def create_page_table(num_pages):
    page_table = {}
    for page in range(num_pages):
        page_table[page] = None
    return page_table
def display_page_table(page_table):
    print("Page Table:")
    print("Page Number\tFrame Number")
    for page, frame in page_table.items():
        print(page, "\t\t", frame if frame is not None else "NULL")

def main():
    storage = int(input("Enter Storage size: "))
    ram = int(input("Enter RAM size: "))
    page_size = int(input("Enter page size: "))
    num_frames = ram // page_size
    num_pages = storage // page_size
    page_table = create_page_table(num_pages)
    display_page_table(page_table)
    next_frame = 0
    while True:
        page_number = int(input("Enter page number to access (-1 to exit):"))
        if page_number == -1:
            break
        if page_number in page_table and page_table[page_number] is not None:
            print("Page", page_number, "executed")
            display_page_table(page_table)
        elif page_number in page_table and page_table[page_number] is None:
            page_table[page_number] = next_frame
            print("Page", page_number, "inserted in frame", next_frame, "and executed")
            next_frame = (next_frame + 1) % num_frames
            display_page_table(page_table)
        else:
            print("Page", page_number, "does not exist!")
if __name__ == "__main__":
    main()