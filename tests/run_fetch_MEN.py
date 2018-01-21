from unittest import TestCase
import web.datasets.similarity as similarity


class TestFetchMEN(TestCase):
    def test_fetch_MEN(self):
        similarity.fetch_MEN()
