MarkdownPage (mdpage)
=====================

A simple html page generator which takes a template file and markdown file as input.

Dependencies
------------

You need to install `markdown2` library.

You will also need to install `argparse` library if you use python with version lower than 2.7.


Installation
------------

Run the `setup.py` script which is contained in this program's directory

```bash
$ sudo python setup.py install
```


Usage
-----

Assume that your template file is index.tp and markdown file is index.md, issue following command to generate index.html:

```bash
$ mdpage -t index.tp -m index.md -o index.html
```

A simple template file for example:

    <html>
    <head>
      <title>Hello world</title>
    </head>
    <body>

    @markdown

    </body>
    </html>

Out put of the markdown file will be inserted at the position where @markdown lies.



