import logging

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Books


@receiver(post_save, sender=Books)
def log_book_updated_added_event(sender, **kwargs):
    logger = logging.getLogger(__name__)
    book = kwargs['instance']
    if kwargs['created']:
        logger.info(f"Книгу додано: {book.name} {book.id=}")
    else:
        logger.info(f"Книгу оновлено: {book.name} {book.id=}")
        
@receiver(post_delete, sender=Books)
def log_book_deleted_event(sender, **kwargs):
    logger = logging.getLogger(__name__)
    book = kwargs['instance']
    logger.info(f"Книгу видалено: {book.name} {book.id=}")
