from celery import shared_task

@shared_task
def multiply(n1, n2):
    return n1 * n2