def getInt(message):
  while True:
    try:
        n = input(f'{message}: ')
        n = int(n)
        if n < 0:
            raise ValueError
        return n
    except:
       print('Please type in a positive integer to proceed!')
       