#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import markdown2
import argparse


class MarkdownParser():
  def __init__(self, tp):
    self.f_tp = open(tp)

  def get_page(self):
    page = ''
    while True:
      line = self.f_tp.readline() 
      if line == '':
        return page
      elif line[0] == '@':
        md_file = line[1:-1]
        try:
          fd = open(md_file, 'r')
        except IOError:
          print 'Cannot find markdown file \"%s\"!!' % md_file
          exit(0)
        page += markdown2.markdown(fd.read())
        continue
      page += line
    return page


def read_args():
  """
  parse arguments
  """
  desc = "MarkdownPage (mdpage) - a simple html page generator."
  parser = argparse.ArgumentParser(description=desc)

  parser.add_argument('-t', '--template-file', type=str, \
      metavar='template_file', dest='tp', action='store', \
      required=True, help="path for template file.")

  parser.add_argument('-o', '--output-file', type=str, \
      metavar='output_file', dest='html_file', action='store', \
      required=True, help="path for output html file.")

  args = parser.parse_args()
  return args

def main():
  args = read_args()
  mp = MarkdownParser(args.tp)
  f_html = open(args.html_file,'w')
  f_html.write(mp.get_page())
  f_html.close()



if __name__ == '__main__':
  main()

