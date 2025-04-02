import os, sys



def get_all_env_vars():
    args = sys.argv[1:]
    env_vars = os.environ

    # Filtering env variables based on passed args
    if args:
        filtered_env_vars = {
            k: v for k, v in env_vars.items() 
            if any(arg in k for arg in args)
        }
    else:
        filtered_env_vars = env_vars

    return filtered_env_vars



def print_all_env_vars():
    env_vars = get_all_env_vars()

    # Printing all env variables in alhpabetical order
    for key in sorted(env_vars):
        print(f'{key}:\t{env_vars[key]}')



if __name__ == '__main__':
    print_all_env_vars()