frame_count = 5
ls = []

def control_page(page):
    if len(ls) < frame_count:
        ls.append(page)
    else:
        ls.pop(0)
        ls.append(page)
    print(f"Pages`  {page} ")

def page_stugum(page):
    print()
    if page in ls:
        print(f"{page} in memory.\n")
    else:
        print(f"{page} not in memory\n")

def display_memory_status():
    print("Memory\n")
    for i, page in enumerate(ls, 1):
        print(f"Frame {i}:  {page}")

def main_foo():

    for i in range(1, 10):
        control_page(f"Page{i}")
    page_stugum("Page1")
    page_stugum("Page7")
    display_memory_status()

main_foo()
