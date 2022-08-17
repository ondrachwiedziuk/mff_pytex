Usage
=====

The Usage contains tutorial, how to create your first document in MFF Pytex, including bibliography, images, tables etc.

First document
--------------

Customarily, we import as follows:

.. code-block:: python

    import mff_pytex as ptx

After this, initialize TeX document:

.. code-block:: python

    texfile = ptx.TexFile('myfile')

Now, you can fill preamble with document and personal details:

.. code-block:: python

    from datetime import date

    preamble = texfile.preamble
    preamble.author = 'John Smith'
    preamble.title = 'My first document'
    preamble.date = date.today()
    preamble.documentclass = ptx.DocumentClass('article')

With filled preamble, let's write some text. Do it as follows:

.. code-block:: python

    body = texfile.document
    body.maketitle()
    body.write('some text')

You can write usual TeX commands using ptx.command, for example '\\section{lists}' looks like:

.. code-block:: python

    body.write(ptx.command('section', 'lists'))

Lists
-----

For creating lists, you can use lists, tuples, dictionaries etc. To write it, use List structure:

.. code-block:: python

    arr = ptx.List(['dog', 'cat'])

You can join it with other lists:

.. code-block:: python

    arr.items(['apple', 'banana'])

And finally, add it do document as follows:

.. code-block:: python

    body.add(arr)

Tables
------

For adding tables in MFF Pytex, we use pandas' dataframe, so at first import pandas and convert your table to pandas' dataframe, than print it:

.. code-block:: python

    import pandas as pd
    import numpy as np

    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    body.add(ptx.Table(s))


Images
------

Adding images is very easy. You don't have to import any package, it is done automatically. Just write:

.. code-block:: python

    image = ptx.Picture('tex.png', caption='My first picture')
    image.write(ptx.command('centering'))
    body.add(image)

Packages
--------

Build-in functions are managed automatically. To add package, just write:

.. code-block:: python

    package = ptx.Package('lipsum')
    ptx.add_package(package)
    body.write(ptx.command('lipsum'))

You can add packages whenever you want, but is recommended to do it at the begining of script.

Bibliography
------------

You can create a bib file same as tex file:

.. code-block:: python

    bib = ptx.Bibliography('sample')
    bib.add(ptx.Book('rome', 'The History of the Decline and Fall of the Roman Empire', 1776, 'Edward Gibbon', 'Strahan and Cadell, London'))
    bib.create()

To citate, just write:

.. code-block:: python

    body.write('My first citation ' + ptx.command('cite', 'rome'))
    body.newpage()
    body.bibliography('sample')

If you want to customize a style of bibbliography list, write as follows:

.. code-block:: python

    preamble.write(ptx.command('bibliographystyle', 'unsrtnat'))

Now, you are ready to use MFF Pytex to write your own document!
