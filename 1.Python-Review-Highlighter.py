# Task 1
reviews = [
        "this product is really good . i'm impressed with its quality .",
        "the performance of this product is excellent . highly recommended !",
        "i had a bad experience with this product . it didn't meet my expectations .",
        "poor quality product . wouldn't recommend it to anyone.",
        "the product was average . nothing extraordinary about it ."
    ]

first_review = (reviews[0])
first_review_replaced_keyword = first_review.replace('good', 'GOOD')
   
second_review = (reviews[1])
second_review_replaced_keyword = second_review.replace('excellent', 'EXCELLENT')

thrid_review = (reviews[2])
thrid_review_replaced_keyword = thrid_review.replace('bad', 'BAD')

forth_review = (reviews[3])
forth_review_replaced_keyword = forth_review.replace('Poor', 'POOR')

fifth_review = (reviews[4])
fifth_review_replaced_keyword = fifth_review.replace('average', 'AVERAGE')

new_reviews = [first_review_replaced_keyword, second_review_replaced_keyword, thrid_review_replaced_keyword, forth_review_replaced_keyword, fifth_review_replaced_keyword]

# print(new_reviews)
    
# Task 2
list_of_words_in_reviews = []

x = first_review.split(" ")
y = second_review.split(" ")
z = thrid_review.split(" ")
a = forth_review.split(" ")
b = fifth_review.split(" ")

list_of_words_in_reviews.extend(x)
list_of_words_in_reviews.extend(y)
list_of_words_in_reviews.extend(z)
list_of_words_in_reviews.extend(a)
list_of_words_in_reviews.extend(b)

postive_keywords = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_keywords = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

counter = {}
for words in list_of_words_in_reviews:
    if words not in counter:
        counter[words] = 0
    counter[words] += 1

p = 0

for word in counter:
    if word in postive_keywords:
        p += 1
        print(p)

n = 0
for word in counter:
    if word in negative_keywords:
        n += 1
        print(n)

# Task 3
# for review in reviews:
#      print(review[0:32] + " ..." )