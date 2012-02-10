MarkdownPage (mdpage)
=====================

A simple html page generator which takes a template file as input.

This script enable you to warp the output of markdown file in html tags you want, so you can write html page with markdown syntax more quickly.


Dependencies
------------

You need to install `markdown` library.

You will also need to install `argparse` library if you use python with version lower than 2.7.


Installation
------------

Run the `setup.py` script which is contained in this program's directory

```bash
$ sudo python setup.py install
```


Usage
-----

Assume that your template file is index.tp, issue following command to generate index.html:

```bash
$ mdpage -t index.tp -o index.html
```

A simple template file for example:

```html
<html>
<head>
  <title>Hello world</title>
</head>
<body>

  <article>
@main.md
  </article>

  <footer>
@foot.md
  </footer>

</body>
</html>
```

Output of main.md file will be inserted in the place where @main.md lies. So will the output of foot.md be inserted in @foot.md.

`foot.md` and `main.md` should be placed in the same directory with `index.tp`.

As you can see, every markdown file name begins with a `@` sign. That's all.



