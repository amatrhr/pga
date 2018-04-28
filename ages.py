print("Hello there, how old are you?")
age_input = int(input("Age in years: "))

## Things you can do: walk, talk, see a PG 13 movie, see an R rated movie, 
## drive, smoke and vote, private gun, gun from a store, pornography store
## get married, drink alcohol
## not live

if age_input >= 0 and age_input < 1:
    print("You basically cannot do anything. How can you read this, little baby?")
elif age_input >= 1 and age_input < 2:
    print("You can probably crawl and stand.")
elif age_input >= 2 and age_input < 5:
    print("You can crawl, stand, walk and talk.")
elif age_input >=5 and age_input < 13 :
    print("You can crawl, stand, walk, talk, see a G rated movie, and read.")
elif age_input >= 13 and age_input < 16:
    print("You can crawl, stand, walk, talk, see a G or PG-13 rated movie, and read.")
elif age_input >= 16 and age_input < 17:
    print("You can crawl, stand, walk, talk, see a G or PG-13 rated movie, read, and apply for a driver's license.")
elif age_input >= 17 and age_input < 18:
    print("You can crawl, stand, walk, talk, see a G, PG-13, or R rated movie, read, and apply for a driver's license.")
elif age_input >= 18 and age_input < 21:
    print("You can crawl, stand, walk, talk, see a G, PG-13, or R rated movie, read, apply for a driver's license, and buy tobacco and prurient goods.")
elif age_input >= 21 and age_input < 35:
    print("You can crawl, stand, walk, talk, see a G, PG-13, or R rated movie, read, apply for a driver's license, and buy tobacco, prurient goods, alcohol, and firearms.")
elif age_input >= 35 and age_input < 55:
    print("You can crawl, stand, walk, talk, see a G, PG-13, or R rated movie, read, apply for a driver's license, buy tobacco, prurient goods, alcohol, and firearms and stand as a candidate for President of the USA.")
elif age_input >= 55 and age_input < 68:
    print("You can crawl, stand, walk, talk, see a G, PG-13, or R rated movie, read, apply for a driver's license, buy tobacco, prurient goods, alcohol, and firearms, stand as a candidate for President of the USA, and live in a retirement community.")
elif age_input >= 68 and age_input < 120:
    print("You can crawl, stand, walk, talk, see a G, PG-13, or R rated movie, read, apply for a driver's license, buy tobacco, prurient goods, alcohol, and firearms, stand as a candidate for President of the USA, live in a retirement community, and get Social Security and Medicare payments.")
elif age_input >= 120:
    print("You are probably dead.")
elif age_input < 0:
    print("You are not yet born. How can you read this?")
else: 
    print("Invalid age (sorry).")

