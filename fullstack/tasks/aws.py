import logging
import os

from fullstack.utils.aws import defaults, get_bucket
from celery import shared_task

logger = logging.getLogger('tasks')

OUTPUT_PATH = 'fullstack/data/'


@shared_task(acks_late=True)
def publish_to_aws(pk):
    key = os.path.join(
        OUTPUT_PATH,
        'data.json'
    )

    bucket = get_bucket()

    bucket.put_object(
        Key=key,
        ACL=defaults.ACL,
        Body='{}',
        CacheControl=defaults.CACHE_HEADER,
        ContentType='application/json'
    )

    logger.info('Published to AWS')
