import camelot

if __name__ == '__main__':
    file = './files/overflowing_columns.pdf'
    t = camelot.read_pdf(file, flavor='stream', split_text=True)
