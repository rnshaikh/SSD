import conf

from src.topup.four_device_plan import FourDevice
from src.topup.ten_device_plan import TenDevice


def device_factory(plan_type):

    plan = {
        conf.FOUR_DEVICE: FourDevice,
        conf.TEN_DEVICE : TenDevice,
    }

    return plan[plan_type]()
