import json
import time

import pytest
import requests
from TestCase.cashier.cashier import Cashier
from common.utils import Utils


class Test_sales:
    salers_body = Cashier.salers_body
    payment_body = Cashier.payment_body

    @pytest.fixture
    def test_sales(self):
            self.headers = Cashier.login(self)
            #货品现销开票
            salers_url = "http://pftest.senguo.me/accountant/sales"
           # headers = Cashier.headers
           # salers_body = Cashier.salers_body

            salers_response = requests.post(salers_url, data = json.dumps(self.salers_body), headers = self.headers)
            time.sleep(0.5)
            if salers_response.status_code == 200:
                print("货品现销开票执行--成功")
            else:
                print("货品现销开票执行--失败")
            salers_json = salers_response.json()
            self.salers_record_ids = salers_json["sales_record_ids"]
            yield self.salers_record_ids
            self.payment()

    def payment(self):
        # 货品现销结算
        payment_url = "http://pftest.senguo.me/accountant/payment"
        payment_response = requests.post(payment_url, data=json.dumps(self.payment_body), headers=self.headers)
        payment_response_json = payment_response.json()
        time.sleep(0.5)
        if payment_response_json["success"] == True:
            print("货品结算--成功")
        else:
            print("货品结算--失败")

    @pytest.mark.usefixtures("test_sales")
    def test_payment_wiht_cash(self,test_sales):
        self.salers_record_ids = test_sales
        self.payment_body["sale_record_ids"] = self.salers_record_ids
        # sale_record_ids = salers_json['sales_record_ids']
        return


    @pytest.mark.usefixtures("test_sales")
    def test_payment_with_bank(self,test_sales):
        self.salers_record_ids = test_sales
        self.payment_body["sale_record_ids"] = self.salers_record_ids
        self.payment_body["fund_account_id"] = "812"
        # sale_record_ids = salers_json['sales_record_ids']
        return

if __name__ == "__main__":
    pytest.main(['test_sales.py','-s'])
   # pytest.main(['test_sales.py', '-s'])

