from utils.testrail import APIClient


class TestRailsReporter():
    def __init__(self):
        self.client = APIClient("")
        self.client.password = ""
        self.client.user = ""

    def send_passed_test_result(self, case_id, comment=None):
        if comment:
            data = dict(status_id=1, comment=comment)
            self.client.send_post(
             'add_result_for_case/{0}/{1}'.format(TESTRAIL_RUN, case_id),
             data
            )
        else:
            data = dict(status_id=1, comment="PASSED")
            # print json.dumps(data)
            self.client.send_post(
             'add_result_for_case/{0}/{1}'.format(TESTRAIL_RUN, case_id),
                data
            )

    def send_failed_testresult(self, case_id, comment=None):
        if comment:
            data = dict(status_id=5, comment=comment)
            self.client.send_post(
             'add_result_for_case/{0}/{1}'.format(TESTRAIL_RUN, case_id),
             data
            )
        else:
            data = dict(status_id=5, comment="FAILED")
            # print json.dumps(data)
            self.client.send_post(
             'add_result_for_case/{0}/{1}'.format(TESTRAIL_RUN, case_id),
                data
            )

    def send_blocked_testresult(self, case_id, comment=None):
        if comment:
            data = dict(status_id=2, comment=comment)
            self.client.send_post(
             'add_result_for_case/{0}/{1}'.format(TESTRAIL_RUN, case_id),
             data
            )
        else:
            data = dict(status_id=2, comment="BLOCKED")
            self.client.send_post(
             'add_result_for_case/{0}/{1}'.format(TESTRAIL_RUN, case_id),
                data
            )