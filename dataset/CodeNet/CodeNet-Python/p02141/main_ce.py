def inpl(): return list(map(int, "6000 5000 20 10 400 300".split()))
W, H, w, h, x, y = inpl()
a = (min(W//2 , x + w//2) + max(-W//2, x-w//2))
b = (min(H//2 , y + h//2) + max(-H//2, y-h//2))
print(b/a)