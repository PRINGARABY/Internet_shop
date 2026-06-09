class Question:
    def __init__(self, question_texst, answer_text, answer_date, question_date, status):
        self.question_text = question_text
        self.answer_text = answer_text
        self.answer_date = answer_date
        self.question_dade = question_date
        self.status = status
    def change_status(self):
        pass

class Review:
    def __init__(self, ration, comment, date):
        self.rating = rating
        self.comment = comment
        self.date = date
