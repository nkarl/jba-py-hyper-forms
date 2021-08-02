from urllib.error import URLError
from hstest import *


class HyperFormsComingSoonTest(DjangoTest):

    def get_index_page(self) -> CheckResult:
        try:
            index_page = self.read_page(self.get_url())
            if "Welcome to the reading club" in index_page:
                return CheckResult.correct()
            return CheckResult.wrong(
                'Index page should contain "Welcome to the reading club" line'
            )
        except URLError:
            return CheckResult.wrong(
                'Cannot connect to the index page.'
            )

    @dynamic_test
    def test_1(self):
        return self.get_index_page()


if __name__ == '__main__':
    HyperFormsComingSoonTest().run_tests()
