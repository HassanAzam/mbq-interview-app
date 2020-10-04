
class Question(models.Model)

    QUESTION_TYPE = (
        (1, "open-text"),
        (2, "true-false"),
        (3, "mcqs")
    )

    id  int
    question_text   string
    question_type   int
    correct_answer  string (it depends on QUESTION_TYPE)

    parent_question_id      by defualt it will be null, could be used to track if question is revised version of another question
    

class QuestionChoice:

    id int
    question_id     FK for questionModel
    choice_value    string


class Interview:

    id int
    interviewer_id      FK to userModel
    question_id         FK to questionModel
    interview_key       random uuid


class InterviewSession:

    id int
    interviewee_id      FK to userModel
    interview_id        FK to interviewModel

class UserAnswer:

    id int
    interview_session       FK to InterviewSession
    question_id             FK to question_id
    QUESTION_TYPE           question_type
    user_answer             answer submitted by user

