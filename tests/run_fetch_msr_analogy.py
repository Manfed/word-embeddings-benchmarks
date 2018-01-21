from unittest import TestCase
import web.datasets.analogy as analogy


class TestFetchMsrAnalogy(TestCase):
    def test_fetch_msr_analogy(self):
        analogy.fetch_msr_analogy()
