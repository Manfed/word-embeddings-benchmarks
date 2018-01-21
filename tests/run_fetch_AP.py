from unittest import TestCase
import web.datasets.categorization as categorization


class TestFetchAP(TestCase):
    def test_fetch_AP(self):
        categorization.fetch_AP()
