from PyPDF2 import PdfFileMerger
from os import listdir, rename
from os.path import isfile, join

####################
# path definitions #
####################

# path of source pdf's
source_path = 'pdfs'
target_path = 'out'
merged_path = 'merged'
file_format = '.pdf'

########
# code #
########

# list of files in the pdfs directory
pdfs = [f for f in listdir(source_path) if isfile(join(source_path, f))]

if len(pdfs) > 1:

    merger = PdfFileMerger()

    # amount of merged pdfs
    count = 0

    for pdf in pdfs:
        if pdf.endswith(file_format):
            merger.append(source_path + '/' + pdf)
            rename(source_path + '/' + pdf, merged_path + '/' + pdf)
            count += 1

    # write output pdf if there are more than 2 source pdfs
    if count > 1:
        merger.write(target_path + "/result.pdf")
        merger.close()
        print('merged ' + str(count) + ' pdfs successful to 1 pdf')
    else:
        print('not enough pdf files. You need at least 2 pdfs')
else:
    print('not enough pdf files. You need at least 2 pdfs')