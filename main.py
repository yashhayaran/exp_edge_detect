# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from detect_edge import experiment

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    images = [
        "assets/photo1717552254.jpeg",
        "assets/TC1-CAM11662615487.305533.jpg"
    ]

    experiment.canny_edge_2(
        images[1]
    )

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
