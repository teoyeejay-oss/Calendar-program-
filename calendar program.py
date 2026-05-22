import os

def check_file():
    if not os.path.exists("diary.txt"):
        open("diary.txt","w").close()
        print("Diary file created")
    else:
        print("The diary file already exists.")

def write_entry():
    txt_data =input("Enter whatever you want to write in the diary file:")
    from datetime import datetime
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    with open("diary.txt","a") as diary_file:
        diary_file.write(f"\n{timestamp}\n{txt_data}\n")

def read_entries():
    with open("diary.txt","r") as diary_file:
        return diary_file.read()

check_file()
while True:
    print("1.Write file")
    print("2.Read file")
    print("3.Exit")
    choice = int(input('Enter your choice: '))
    if choice ==1:
        write_entry()
    elif choice ==2:
        print(read_entries())
    elif choice ==3:
        break




