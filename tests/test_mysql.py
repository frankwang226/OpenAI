import pytest

from src.hogwarts_ai_testing.LC_demo.SQL.mysql import mysql


class TestMySQL:
    @pytest.mark.parametrize("question", ["mall_sales_order表的Id关联mall_sales_order_dtl表的OrderId，请问品牌739，最近一个月的卖出最多的商品是哪件，给出商品名称？"])
    def test_mysql(self, question):
        result = mysql(question)
        print(result)
