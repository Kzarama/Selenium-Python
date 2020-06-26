from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTests
from searchtests import SearchTest

assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([assertions_test, search_test])

kwargs = {
    'output': 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)