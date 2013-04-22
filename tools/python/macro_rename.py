#!/bin/python
"""
This script is used to correct '#ifndef XXX' in C++ header file.

For example, if a C++ header file is src/a/b/c.h, if your run this script in the
src directory, the correct #ifnef should be:

  #ifndef A_B_C_H_
  #define A_B_C_H_
  // ...
  #endif  // A_B_C_H_

"""
import os
import sys
from optparse import OptionParser

IFNDEF_MACRO_NAME = "#ifndef";
BACKUP_EXTENSION_NAME = ".bak";

def RenameInclusionMacro(header_filename):
  print "Processing ", header_filename, " ...";
  header_file = open(header_filename, "r");
  content = header_file.read();
  header_file.close();

  index = content.find(IFNDEF_MACRO_NAME);
  if (index == -1):
    print "Warning: No #ifndef macro found in ", header_filename;
    return;

  # Try to get the inclusion macro definition.
  start_index = index + len(IFNDEF_MACRO_NAME) + 1;
  end_index = content[start_index:].find("\n") + start_index;
  macro_def = content[start_index:end_index];

  # Concat the new macro definition.
  filepath = header_filename;
  new_macro_def = filepath.replace('/', '_').replace('.', '_').upper() + '_';

  # Replace the old one with the new one.
  if new_macro_def == macro_def:
    return;
  new_content = content.replace(macro_def, new_macro_def);

  header_file = open(header_filename, "w");
  header_file.write(new_content);
  header_file.close();

def main():
  usage = "macro_rename.py dirname"
  parser = OptionParser("macro_rename.py [options]");
  (options, args) = parser.parse_args();

  if len(args) < 1:
    print parser.usage;

  pathname = args[0];
  if not os.path.exists(pathname):
    raise Exception("File Not Found: " + pathname)

  if os.path.isfile(pathname):
    RenameInclusionMacro(pathname);
  else:
    for root, dirs, files in os.walk(pathname):
      for f in files:
        if f.endswith(".h"):
          RenameInclusionMacro(os.path.join(root, f))

if __name__ == "__main__":
  sys.exit(main());

