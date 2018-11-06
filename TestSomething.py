import logging

import allure
import pytest
from hamcrest import assert_that, any_of

from steps.Steps import make_request


@pytest.mark.usefixtures('prepare_env')
class TestNewApp(object):
    logger = logging.getLogger(__name__)
    logger.info("Started")
    variable_from_test = 'Hoohohohohoh!'


    @allure.step
    @pytest.mark.case('3461527')
    @pytest.mark.dns
    def test_something(self):
        """Test checks that record for restricted zone was not created for default tag"""
        self.logger.info(self.test_something.__name__ + " STARTED")
        code = make_request("get", "https://www.tut.by", return_code="yes")

        assert_that(code, any_of(400, 401, 404, 422),'Record for restricted DNS zone was created')
        # self.logger.info(self.test_something.__name__ + " FINISHED")

