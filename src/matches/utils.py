from django.contrib.auth import get_user_model
from questions.models import UserAnswer

User = get_user_model()
users = User.objects.all()
all_user_answers = UserAnswer.objects.all()

yemalin =users[0]
caden =users[1]


def get_points(user_a, user_b):
  	a_answers = UserAnswer.objects.filter(user = user_a)
	b_answers = UserAnswer.objects.filter(user = user_b)
	a_total_awarded   = 0
	a_points_possible = 0
	num_questions = 0
	for a in a_answers:
		for b in b_answers:
			if a.question.id == b.question.id:
				a_pref   = a.their_answer
				b_answer = b.my_answer
				num_questions += 1
				if a_pred == b_answer:
					'''
					awards potin for correct b_answer
					'''
					a_total_awarded += a.their_points
					'''
					assiging total their_points
					'''
				a_points_possible += a.their_points
	percent =a_total_awarded/Decimal(a_points_possible)
	if percent ==0:
		percent = 0.00001
	return percent,  num_questions

	'''
def get_match(user_a, user_b):
	user_a_answers = UserAnswer.objects.filter(user = user_a)[1]
	user_b_answers = UserAnswer.objects.filter(user = user_b)[0]
	if user_a_answers.question.id == user_b_answers.question.id:
		user_a_answer = user_a_answers.my_answer
		user_a_pref   = user_a_answers.their_answer
		user_b_answer = user_b_answers.my_answer
		user_b_pref   = user_b_answers.their_answer
		if user_a_answer == user_b_pref:
			print"%s fits %s's preference" %(user_a_answers.user.username, user_b_answers.user.username)
		if user_a_pref == user_b_answer:
			print"%s fits %s's preference" %(user_a_answers.user.username, user_b_answers.user.username)
		if user_a_answer == user_b_pref and user_a_pref == user_b_answer:
			print "Ideal Match"



'''