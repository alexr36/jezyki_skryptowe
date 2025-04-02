import sys, os, datetime, mimetypes, json



def read_args():
    if len(sys.argv) < 3:
        sys.stderr.write(
            "[ERROR] Not enough arguments. "
            "Usage: python mediaconvert.py <directory> <format>"
        )
        exit(1)

    return sys.argv[1:]  



def get_output_dir():
    return os.environ.get('CONVERTED_DIR', os.path.join(os.getcwd(), 'converted'))



def ensure_dir(path):
    os.makedirs(path, exist_ok=True)



def extract_file_type(filepath):
    return mimetypes.guess_type(filepath)[0]



def is_video_or_audio(filepath):
    type = extract_file_type(filepath)
    return type and (type.startswith('audio') or type.startswith('video'))



def is_image(filepath):
    type = extract_file_type(filepath)
    return type and type.startswith('image')



def add_ts_and_ext(filename, extension):
    return add_extension(add_timestamp(filename), extension)



def add_timestamp(filename):
    name = os.path.basename(os.path.splitext(filename)[0])
    timestamp = datetime.datetime.now().strftime('%Y%m%d')
    return f"{timestamp}-{name}"



def add_extension(filename, extension):
    name, _ = os.path.splitext(filename)
    return f"{name}.{extension}"



def log_history(history_file, entry):
    history = []

    if os.path.exists(history_file):
        with open(history_file, 'r') as file:
            history = json.load(file)
    
    history.append(entry)

    with open(history_file, 'w') as file:
        json.dump(history, file, indent=2)
