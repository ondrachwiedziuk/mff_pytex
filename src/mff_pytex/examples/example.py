import mff_pytex as ptx
from datetime import date


texfile = ptx.TexFile('myfile')

preamble = texfile.preamble
preamble.author = 'John Smith'
preamble.title = 'My fist document'
preamble.date = date.today()
preamble.documentclass = ptx.DocumentClass('arcticle')

texfile.create()

texfile.make_pdf()
