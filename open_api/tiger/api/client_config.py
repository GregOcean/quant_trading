from tigeropen.common.consts import (Language,        # 语言
                                Market,           # 市场
                                BarPeriod,        # k线周期
                                QuoteRight)       # 复权类型
from tigeropen.tiger_open_config import TigerOpenClientConfig
from tigeropen.common.util.signature_utils import read_private_key
from tigeropen.quote.quote_client import QuoteClient
import logging


class ClientConfig(object):
    def __init__(self):
        # 调用下方定义的函数生成用户配置ClientConfig对象
        self.client_config = ClientConfig.get_client_config()
        # 私钥也可填字符内容
        # self.client_config.private_key = 'MIICWwIBAAKBgQCSW+.....私钥内容'

        # 日志级别及路径
        self.client_config.log_level = logging.DEBUG  # 需 import logging
        self.client_config.log_path = '/Users/yang.wang/Documents/QuantTrading/quant_trade_real_operation/open_api/log/tigerapi.log'

        # 语言
        self.client_config.language = 'zh_CN'
        # 时区
        self.client_config.timezone = 'US/Eastern'

        # 接口超时时间
        self.client_config.timeout = 15
        # 超时重试设置
        # 最长重试时间，单位秒
        self.client_config.retry_max_time = 60
        # 最多重试次数
        self.client_config.retry_max_tries = 2

        # 2FA token 刷新间隔, 单位秒。设置为0则不自动刷新
        self.client_config.token_refresh_duration = 24 * 60 * 60


    @staticmethod
    def get_client_config():
        """
        https://quant.itigerup.com/#developer 开发者信息获取
        """
        # 港股牌照需用 props_path 参数指定token路径，如 '/Users/xxx/xxx/', 如不指定则取当前路径
        client_config = TigerOpenClientConfig(props_path='/Users/yang.wang/Documents/QuantTrading/quant_trade_real_operation/open_api/tiger/config/tiger_openapi_config.properties')
        return client_config


