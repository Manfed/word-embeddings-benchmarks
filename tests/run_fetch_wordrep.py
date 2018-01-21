from unittest import TestCase
import web.datasets.analogy as analogy


class RunFetchWordrep(TestCase):
    def test_fetch_wordrep(self):
        analogy.fetch_wordrep()
