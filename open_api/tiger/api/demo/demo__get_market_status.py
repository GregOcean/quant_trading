
from tigeropen.common.consts import (Language,        # 语言
                                Market,           # 市场
                                BarPeriod,        # k线周期
                                QuoteRight)       # 复权类型
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
from open_api.tiger.api.client_config import ClientConfig
# 查询行情的操作通过QuoteClient对象的成员方法实现，所以调用相关行情接口之前需要先初始化QuoteClient，具体代码如下：
# 首先通过自定义的函数生成配置文件, 函数get_client_config会返回一个包含初始化行情对象所需要的用户信息的ClientConfig对象
# 用来传入行情对象QuoteClient构造函数中，以进行QuoteClient的初始化。
# 也可选择使用tigeropen.tiger_open_config.get_client_config()函数生成用户配置对象


# 调用上方定义的函数生成用户配置ClientConfig对象
client_config_obj = ClientConfig()

# 随后传入配置参数对象来初始化QuoteClient
quote_client = QuoteClient(client_config_obj.client_config)

# 完成初始化后，就可以调用quote_client方法来使用调用QuoteClient对象的get_stock_brief方法来查询股票行情了
# 此处以美国股票为例，关于其他支持的市场及标的类型，请参考文档的基本操作部分。
# 对于使用多台设备调用API的用户，需先调用grab_quote_permission进行行情权限的抢占，详情请见基本操作-行情类-通用-grab_quote_permission方法说明
permissions = quote_client.grab_quote_permission()

#输出list类型的行情权限权限列表
print(permissions)

market_status_list = quote_client.get_market_status(Market.US)

# 查看属性
market_status = market_status_list[0]
print(market_status.market)
print(market_status.trading_status)
