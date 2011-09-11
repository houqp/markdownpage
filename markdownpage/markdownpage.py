#!/usr/bin/env/ python
# -*- coding: utf-8 -*-

import markdown2
import argparse

class MarkdownParser():
  def __init__(self, md, tp):
    self.f_md = open(md)
    self.f_tp = open(tp)

  def get_page(self):
    page = ''

    while True:
      line = self.f_tp.readline() 
      if line == '@markdown\n':
        break
      if line == '':
        return page
      page += line

    page += markdown2.markdown(self.f_md.read())

    page += self.f_tp.read()
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

  parser.add_argument('-m', '--markdown-file', type=str, \
      metavar='markdown_file', dest='md', action='store', \
      required=True, help="path for markdown file.")

  parser.add_argument('-o', '--output-file', type=str, \
      metavar='output_file', dest='html_file', action='store', \
      required=True, help="path for output html file.")

  args = parser.parse_args()
  return args


def main():
  args = read_args()
  mp = MarkdownParser(args.md, args.tp)
  f_html = open(args.html_file,'w')
  f_html.write(mp.get_page())
  f_html.close()


if __name__ == '__main__':
  main()

