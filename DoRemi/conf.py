INVALID_DATE = "INVALID_DATE"
SUBSCRIPTIONS_NOT_FOUND = "SUBSCRIPTIONS_NOT_FOUND"
ADD_SUBSCRIPTION_FAILED = "ADD_SUBSCRIPTION_FAILED"
DUPLICATE_CATEGORY = "DUPLICATE_CATEGORY"
ADD_TOPUP_FAILED = "ADD_TOPUP_FAILED"
DUPLICATE_TOPUP = "DUPLICATE_TOPUP"

INIT_ONE = 1
INIT_ZERO = 0

STREAMING = {
    "VIDEO": {
        "FREE": {
            "month": 1,
            "cost": 0
        },
        "PERSONAL": {
            "month": 1,
            "cost": 200
        },
        "PREMIUM":{
            "month": 3,
            "cost": 500
        }
    },
    "PODCAST": {
        "FREE": {
            "month": 1,
            "cost": 0
        },
        "PERSONAL": {
            "month": 1,
            "cost": 100
        },
        "PREMIUM":{
            "month": 3,
            "cost": 300
        }    
    },
    "MUSIC": {
        "FREE": {
            "month": 1,
            "cost": 0
        },
        "PERSONAL": {
            "month": 1,
            "cost": 100
        },
        "PREMIUM":{
            "month": 3,
            "cost": 250
        }    
    }
}

TOPUP = {
    "FOUR_DEVICE": {
        "device": 4,
        "month": 1,
        "cost": 50
    },
    "TEN_DEVICE": {
        "device": 10,
        "month": 1,
        "cost": 100
    }
}

COMMANDS = {
    "START_SUBSCRIPTION": "start_subscription_handler",
    "ADD_SUBSCRIPTION": "add_subscription_handler",
    "ADD_TOPUP": "add_topup_handler",
    "PRINT_RENEWAL_DETAILS": "print_renewal_info_handler"
}

RENEWAL_REMINDER_STR = "RENEWAL_REMINDER {category} {date}"
RENEWAL_AMOUNT_STR = "RENEWAL_AMOUNT {cost}"

REMINDER_DAY = 10