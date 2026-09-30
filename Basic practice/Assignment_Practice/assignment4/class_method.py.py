class book:
    def __init__(self, title, author, listofreview):
        self.title = title
        self.author = author
        self.listofreview = listofreview

    def add_new_review(self):
        r = input("Add your review: ")
        self.listofreview.append(r)

    def count_review(self):
        print("total review: ", len(self.listofreview))

    def all_reviews(self):
        print("All review: ")
        for review in self.listofreview:
            print(review)


b1 = book("python", "guido", [])

b1.add_new_review()
b1.add_new_review()
b1.count_review()
b1.all_reviews()