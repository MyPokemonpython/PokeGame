import redis


class TriviaService:
    def __init__(self):
        self.redis_client = redis.Redis(host='localhost', port=6379, db=0)

    def set_score(self, user_id, score):
        self.redis_client.set(f"score:{user_id}", score)

    def get_score(self, user_id):
        score = self.redis_client.get(f"score:{user_id}")
        if score is None:
            return 0
        return int(score)

    def check_answer(self, question_id, answer):
        question = self.questions_data.get(question_id)
        if question and question["correct_answer"] == answer:
            return True
        return False

    def is_valid_answer(self, question_id, answer):
        question = self.question_data.get(question_id)
        if question and answer in question["valid_answer"]:
            return True
        return False



