import allure
import pytest
import allure_pytest

@pytest.fixture
def iniy():
    print("我是前置")
    yield
    print("我是后置")

@allure.story("test_01")
@pytest.mark.usefixtures("iniy")
class TestCase:

    def test_1(self):
        print("我是测试用例1")

    def test_ha(self):
        print("我说测试用例2")


if __name__ == '__main__':
    pytest.main(['--allure_stories=test_01'])




