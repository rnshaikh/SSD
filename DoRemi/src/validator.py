import conf


def validate_add_top_up_subscription(is_valid, subscriptions, topup):

    if not is_valid:
        return conf.ADD_TOPUP_FAILED + " " + conf.INVALID_DATE

    if not len(subscriptions):
        return conf.ADD_TOPUP_FAILED + " " + conf.SUBSCRIPTIONS_NOT_FOUND

    if topup:
        return conf.ADD_TOPUP_FAILED + " " + conf.DUPLICATE_TOPUP


def validate_add_streaming_subscription(is_valid, subscriptions, category):

    if not is_valid:
            return conf.ADD_SUBSCRIPTION_FAILED + " " + conf.INVALID_DATE
  
    if category in subscriptions:
        return conf.ADD_SUBSCRIPTION_FAILED + " " + conf.DUPLICATE_CATEGORY
