question = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ')

question = question.upper().strip()

if (question == '42') or (question == 'FORTY TWO') or (question == 'FORTY-TWO'):
    print('Yes')
else:
    print('No')