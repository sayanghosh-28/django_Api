from celery import shared_task
import logging

logger = logging.getLogger(__name__)

#@shared_task(bind=True)
@shared_task(name='crypto.tasks.test_talk')
def test_task(coin):
    logger.info(f"Starting test task for coin: {coin}")
    try:
        # Simulate a successful task execution
        result = {"coin": coin, "data": f"Sample data for {coin}"}
        logger.info(f"Task completed for coin: {coin}, result: {result}")
        return result
    except Exception as e:
        logger.error(f"Exception in task for coin: {coin}, error: {e}")
        return {"error": str(e)}
