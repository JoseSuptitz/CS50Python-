name = input('File name: ').upper().strip()

if name.endswith('GIF'):
    print('image/gif')
elif name.endswith('JPG'):
    print('image/jpeg')
elif name.endswith('JPEG'):
    print('image/jpeg')
elif name.endswith('PNG'):
    print('image/png')
elif name.endswith('PDF'):
    print('application/pdf')
elif name.endswith('TXT'):
    print('text/plain')
elif name.endswith('ZIP'):
    print('	application/zip')
else:
    print('application/octet-stream')

