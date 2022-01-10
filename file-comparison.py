import os
from difflib import SequenceMatcher

folder_path = "/files_to_compare"
file_paths = []
matched_files = []

# Add all paths of files found in folder to list
for r, d, f in os.walk(folder_path):
    for file in f:
        file_paths.append(os.path.join(r, file))

# Compare all files with each other (O = n**2)
for file1_path in range(len(file_paths)):
    file1 = open(file_paths[file1_path]).read()
    for file2_path in range(len(file_paths)):
        # Don't compare the same file
        if file1_path != file2_path:
            file2 = open(file_paths[file2_path]).read()
            match = SequenceMatcher(None, file1, file2)
            # Calculate ratio of similarity between files
            # Returned range 0.0-1.0 where 0.0 is totally different and 1.0 means files are identical
            quick_ratio = match.quick_ratio()
            # If ratio is bigger than 80% print ratio and file names
            if quick_ratio > 0.8:
                print(f"Match found ({quick_ratio * 100} %): '{file_paths[file1_path]}' | '{file_paths[file2_path]}'")
                matched_files.append(file_paths[file2_path])
            # Underline identical files to not omit them in console
            if quick_ratio == 1.0:
                print("^^^^^^^^^^^^^^^^^^^^^^^ EXACT SAME FILE ^^^^^^^^^^^^^^^^^^^^^^^")

# Remove duplicates from list of matched files
matched_files = list(set(matched_files))

# Print all files where similarity is more than 80%
print("###########################################")
for m in matched_files:
    print(m)
