prizes=[120,250,300,125,100,90]
def order_prizes(prizes):
    return sorted(prizes,reverse=True)
print("Ordered prizes:", order_prizes(prizes))
