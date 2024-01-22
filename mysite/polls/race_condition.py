import threading

from django.db.models import F

from .models import Choice, Question


def like():
    que = Question.objects.first()
    option = que.choice_set.first()
    option.votes = F("votes") + 1
    option.save()


def thread_task():
    for i in range(20):
        like()


def main():
    que = Question.objects.first()
    option = que.choice_set.first()
    option.votes = 0
    option.save()

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    t1.start()
    t2.start()

    t1.join()
    t2.join()


for i in range(3):
    main()
    print(f"Iteration {i} vote counter: {Choice.objects.first().votes}")
