import sys, os, time, argparse



def parse_args():
    parser = argparse.ArgumentParser(description="Simplified Unix tail implementation in Python")
    parser.add_argument('filename', nargs='?', help="File to read (optional)")
    parser.add_argument('--lines', type=int, default=10, help="Number of lines to show (optional)")
    parser.add_argument('--follow', action='store_true', help="Follow file as it grows (optional)")

    return parser.parse_args()



def read_from_stdin():
    return sys.stdin.readlines()



def read_from_file(filename):
    with open(filename) as file:
        return file.readlines()



def display_tail(lines, n):
    for line in lines[-n:]:
        print(line.rstrip())



def follow_file(filename):
    with open(filename) as file:
        file.seek(0, os.SEEK_END)

        try:
            while True:
                if file.tell() > os.stat(filename).st_size:
                    file.seek(0, os.SEEK_END)

                line = file.readline()
            
                if not line:
                    time.sleep(0.5)    # Wait for 0.5s
                    continue

                print(line.rstrip())
        except KeyboardInterrupt:
            print(f"[INFO] Stopped following the file '{filename}'")
            return    



def main():
    args = parse_args()
    filename = args.filename
    lines = args.lines

    if filename:
        if not os.path.isfile((filename)):
            sys.stderr.write((f"[ERROR] File '{filename}' not found\n"))
            sys.exit(1)

        display_tail(read_from_file(filename), lines)

        if args.follow:
            follow_file(filename)
    else:
        if sys.stdin.isatty():
            sys.stderr.write(f"[ERROR] No input provided. Use a pipe or provide a file\n")
            sys.exit(1)

        display_tail(read_from_stdin(), lines)   
      
            

if __name__ == '__main__':
    main()
