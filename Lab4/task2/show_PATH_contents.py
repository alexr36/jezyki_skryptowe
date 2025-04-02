import sys, os



def determine_solution():
    if len(sys.argv) < 2:
        sys.stderr.write("[ERROR] Please provide a parameter\n")
        return

    param = sys.argv[1]

    if param == '-dirs':
        show_only_directories()
    elif param == '-contents':
        show_directories_with_contents()
    else:
        sys.stderr.write(f"[ERROR] Unknown parameter: {param}\n")



def extract_dirs():
    return os.environ.get('PATH').split(os.pathsep)


# When passed '-dirs'
def show_only_directories():
    dirs = extract_dirs()

    for dir in dirs:
        print(dir)


# When passed '-contents'
def show_directories_with_contents():
    dirs = extract_dirs()

    for dir in dirs:
        print(f"{dir}:")

        if not os.path.isdir(dir):
            print("[INFO] Not a directory or inaccessible")
            continue

        print(os.listdir(dir))
            


if __name__ == '__main__':
    determine_solution()
