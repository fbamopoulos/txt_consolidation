import glob
from os import path


def consolidate_files(file_extension, directory_path):
    """
    :param file_extension: File extension of file to be consolidated
    :param directory_path: Directory to look for files to consolidate
    :return: 0 if no errors, -1 if error
    """

    my_file_paths = glob.glob(path.join(directory_path, '*'+file_extension))
    print('Found {} {} files'.format(len(my_file_paths), file_extension))

    if not my_file_paths:
        print('No files to process')
        return -1

    sum_file = open(path.join(directory_path, 'sumFile.txt'), 'a', encoding='utf-8')

    for file_path in my_file_paths:
        print('Processing:', file_path)
        with open(file_path, 'r', encoding='utf-8') as f:
            input_lines = f.readlines()
        sum_file.writelines(input_lines)

    sum_file.close()
    return 0


if __name__ == '__main__':
    consolidate_files('.txt', '.')
