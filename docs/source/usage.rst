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
    preamble.title = 'My fist document'
    preamble.date = date.today()
    preamble.documentclass = ptx.DocumentClass('arcticle')

With filled preamble, let's write some text. Do it as follows:

.. code-block:: python

    body = texfile.document
    body.maketititle()
    body.write('some text')
