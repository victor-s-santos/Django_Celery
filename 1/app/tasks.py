from celery import shared_task

@shared_task
def multiply(n1, n2):
    return n1 * n2

@shared_task
def send_email(email_address):
    """Lógica para enviar o email aqui"""
    