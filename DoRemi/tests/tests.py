import conf 

from unittest import TestCase

from src.streaming_app import Subscription



class SubscriptionTest(TestCase):


    @classmethod
    def setUp(cls):
        cls.subscription = Subscription()
        cls.start_date = "22-12-2022"
        cls.invalid_start_date = "2022-12-22"

    def test_start_subscription(self):
        self.subscription.start_subscription(self.start_date)
        self.assertTrue(self.subscription.is_valid, True)

    def test_start_subscription_fail(self):
        self.subscription.start_subscription(self.invalid_start_date)
        self.assertFalse(self.subscription.is_valid)

    def test_subscription_video_free(self):
        self.subscription.start_subscription(self.start_date)
        self.subscription.add_streaming_subscription(conf.VIDEO, conf.FREE)
        ans, cost, error = self.subscription.get_renewal_info()
        self.assertEqual(ans[conf.VIDEO], "12-01-2023")

    def test_subscription_video_personal(self):
        self.subscription.start_subscription(self.start_date)
        self.subscription.add_streaming_subscription(conf.VIDEO, conf.PERSONAL)
        ans, cost, error = self.subscription.get_renewal_info()
        self.assertEqual(cost, conf.PERSONAL_VIDEO_COST)

    def test_add_subscription_fail(self):

        self.subscription.start_subscription(self.start_date)
        self.subscription.add_streaming_subscription(conf.VIDEO, conf.PERSONAL)
        error = self.subscription.add_streaming_subscription(conf.VIDEO, conf.PERSONAL)
        self.assertEqual(error, conf.ADD_SUBSCRIPTION_FAILED+" "+conf.DUPLICATE_CATEGORY)

    def test_add_top_up_subscription(self):

        self.subscription.start_subscription(self.start_date)
        self.subscription.add_streaming_subscription(conf.VIDEO, conf.PERSONAL)
        self.subscription.add_top_up_subscription(conf.FOUR_DEVICE, 2)
        ans, cost, error = self.subscription.get_renewal_info()
        self.assertEqual(cost, conf.PERSONAL_VIDEO_COST+(conf.FOUR_DEVICE_COST*2))

    def test_add_top_up_subscription_fail(self):

        self.subscription.start_subscription(self.start_date)
        self.subscription.add_streaming_subscription(conf.VIDEO, conf.PERSONAL)
        self.subscription.add_top_up_subscription(conf.FOUR_DEVICE, 2)
        error = self.subscription.add_top_up_subscription(conf.TEN_DEVICE, 2)
        self.assertEqual(error, conf.ADD_TOPUP_FAILED+" "+conf.DUPLICATE_TOPUP)


















