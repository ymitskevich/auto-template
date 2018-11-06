import pytest

from pytest import fixture
import logging
import sys
import allure

from utils import TestRailsReporter
# reporter = TestRailsReporter("")

import os

logging.basicConfig(level=logging.INFO, format="""\n########%(asctime)s %(name)-12s %(levelname)-8s %(message)s'\n""",
                    stream=sys.stdout)
logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("paramiko").setLevel(logging.WARNING)



@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    dir(outcome)
    rep = outcome.get_result()


    if item.get_marker('case'):
        print "---------------------"
        print dir(item)
        print item.get_marker('case').args[0]
        case_id = item.get_marker('case').args[0]
        print case_id
        print "---------------------"

        if rep.when == "call" and rep.failed:
            comment = "FAILED REASON:\n" + str(call.excinfo.value)
            # reporter.send_failed_testresult(case_id, comment)
        elif rep.when == "call" and rep.passed:
            comment = "PASSED"
            # reporter.send_passed_test_result(case_id, comment)

def pytest_exception_interact(node, call, report):
    if report.failed:
        print "_________________________________"
        return call.excinfo


@fixture(scope='class')
def prepare_env(request):
    logger = logging.getLogger(prepare_env.__name__)
    logger.info("STARTED TEST")
    variable_from_test = request.cls.variable_from_test
    print ("##########" + variable_from_test + "#######################")
