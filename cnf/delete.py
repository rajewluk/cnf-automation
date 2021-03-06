import logging

from onapsdk.aai.business import Customer

from config import Config

logger = logging.getLogger("")
logger.setLevel(logging.DEBUG)
fh = logging.StreamHandler()
fh_formatter = logging.Formatter('%(asctime)s %(levelname)s %(lineno)d:%(filename)s(%(process)d) - %(message)s')
fh.setFormatter(fh_formatter)
logger.addHandler(fh)

logger.info("******** Get Customer *******")
customer = None
try:
    customer = Customer.get_by_global_customer_id(Config.GLOBAL_CUSTOMER_ID)
except:
    logger.error("Customer not found")
    exit(1)

logger.info("******** Check Service Subscription *******")
service_subscription = None
for service_sub in customer.service_subscriptions:
    if service_sub.service_type == Config.SERVICENAME:
        logger.info("Service %s subscribed", Config.SERVICENAME)
        service_subscription = service_sub
        break
if not service_subscription:
    logger.error("Service Subscription not found")
    exit(1)

logger.info("******** Get Service Instance details *******")
service_instance = None
for service in service_subscription.service_instances:
    if service.instance_name == Config.SERVICE_INSTANCE_NAME:
        service_instance = service
        break
if not service_instance:
    logger.error("Service Instance not found")
    exit(1)

logger.info("******** Delete Service %s *******", service_instance.instance_name)
service_deletion = service_instance.delete()