

def rabin_karp(word, pattern, d, q):
    wl = len(word)
    pl = len(pattern)
    h = 1
    p = 0
    t = 0
    result = []

    for i in range(pl-1):
        h = (h*d) % q

    for i in range(pl):
        p = (d*p + ord(pattern[i])) % q
        t = (d*t + ord(word[i])) % q

    for s in range(wl-pl+1):
        if p == t:
            match = True
            for i in range(pl):
                if pattern[i] != word[s+i]:
                    match = False
                    break
            if match:
                result = result + [s]
        if s < wl-pl:
            t = (t-h * ord(word[s])) % q  #rmove letter s
            t = (t*d + ord(word[s + pl])) % q # remover letter s+pl
            t = (t+q) % q  # make sure t>=0
    return result





