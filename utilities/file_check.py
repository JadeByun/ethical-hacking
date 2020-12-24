def file_check(filepath):
    try:
        return open(filepath, "r")
    except IOError:
        print('Error: File does not appear to exist.')
        return 0
