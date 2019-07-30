import os

string_path = os.path.abspath('.')
string_path = os.path.join(string_path, 'files_to_insert')

for unk_root, unk_dir, unk_files in os.walk(string_path):
    print('root: %s' %unk_root)
    print('dir: %s' %unk_dir)
    print('files: %s\n' %unk_files)