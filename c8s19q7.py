

def reverse(s):
    """
      >>> reverse('happy')
      'yppah'
      >>> reverse('Python')
      'nohtyP'
      >>> reverse("")
      ''
      >>> reverse("P")
      'P'
    """
    last = ""
    x = 1
    while x <= len(s):
        lastoutput = s[-x]
        last += lastoutput
        x += 1
    return last
 
if __name__ == '__main__':
    import doctest
    doctest.testmod()