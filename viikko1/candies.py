""" 
Nallekarkki maksaa a euroa ja suklaakarkki maksaa b euroa. Montako karkkia voit ostaa enintään, jos sinulla on yhteensä rahaa c euroa?
Voit olettaa, että a, b ja c ovat kokonaislukuja välillä 1 - 100.
Toteuta tiedostoon candies.py funktio count, joka antaa suurimman karkkien määrän.
 """

def count(a, b, c):
    if a < b:
        return c // a
    else :
        return c // b

if __name__ == "__main__":
    print(count(3, 4, 11)) # 3
    print(count(5, 1, 100)) # 100
    print(count(2, 3, 1)) # 0
    print(count(2, 3, 9)) # 4