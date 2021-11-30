#!/usr/bin/python3

import argparse
from argparse import RawTextHelpFormatter
import sys
from asf_metadata import iso_template2lists, iso_xml_structure, \
  meta_xml_file, iso_dictionary_structure, meta_json_file


# Wrapper for the command line version
def generate_iso_template(excelFile, isoBase):

  ### Extract ISO template from Excel spreadsheet
  print('\nExtracting ISO metadata template from Excel spreadsheet ...')
  (isoTemplate, isoParams, isoValues) = \
    iso_template2lists(excelFile, 'ISO Metadata Structure')

  ### Write ISO template to files
  print('Writing ISO metadata template to files ...')
  isoStructure = \
    iso_xml_structure(excelFile, isoTemplate, isoParams, isoValues, True)
  meta_xml_file(isoStructure, isoBase + '.xml')
  isoStructure = \
    iso_dictionary_structure(excelFile, isoTemplate, isoParams, isoValues)
  meta_json_file(isoStructure, isoBase + '.json')


if __name__ == '__main__':

  parser = argparse.ArgumentParser(prog='generate_iso_template.py',
    description='Generate ISO template file from Excel spreadsheet',
    formatter_class=RawTextHelpFormatter)
  parser.add_argument('excelFile', 
    help='name of the Excel template spreadsheet')
  parser.add_argument('isoBase', 
    help='basename of the ISO metadata template file')
  if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)
  args = parser.parse_args()

  generate_iso_template(args.excelFile, args.isoBase)
