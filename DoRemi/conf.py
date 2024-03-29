INVALID_DATE = "INVALID_DATE"
SUBSCRIPTIONS_NOT_FOUND = "SUBSCRIPTIONS_NOT_FOUND"
ADD_SUBSCRIPTION_FAILED = "ADD_SUBSCRIPTION_FAILED"
DUPLICATE_CATEGORY = "DUPLICATE_CATEGORY"
ADD_TOPUP_FAILED = "ADD_TOPUP_FAILED"
DUPLICATE_TOPUP = "DUPLICATE_TOPUP"

INIT_ONE = 1
INIT_ZERO = 0

FREE_MONTH = 1 
FREE_COST = 0
PERSONAL_MONTH = 1
PERSONAL_VIDEO_COST = 200
PREMIUM_VIDEO_MONTH = 3
PREMIUM_VIDEO_COST = 500
PERSONAL_MUSIC_COST = 100
PREMIUM_MUSIC_MONTH = 3
PREMIUM_MUSIC_COST = 250
PERSONAL_PODCAST_COST = 100
PREMIUM_PODCAST_MONTH = 3
PREMIUM_PODCAST_COST = 300
FOUR_DEVICE_COST = 50
TEN_DEVICE_COST = 100

FREE = "FREE" 
PERSONAL = "PERSONAL"
PREMIUM = "PREMIUM"

FOUR_DEVICE = "FOUR_DEVICE"
TEN_DEVICE = "TEN_DEVICE"

MUSIC = "MUSIC"
VIDEO = "VIDEO"
PODCAST = "PODCAST"


COMMANDS = {
    "START_SUBSCRIPTION": "start_subscription_handler",
    "ADD_SUBSCRIPTION": "add_subscription_handler",
    "ADD_TOPUP": "add_topup_handler",
    "PRINT_RENEWAL_DETAILS": "print_renewal_info_handler"
}

RENEWAL_REMINDER_STR = "RENEWAL_REMINDER {category} {date}"
RENEWAL_AMOUNT_STR = "RENEWAL_AMOUNT {cost}"

REMINDER_DAY = 10

DATE_FORMAT = "%d-%m-%Y"