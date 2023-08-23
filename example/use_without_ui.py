import datetime
from extensible_calendar.base_calendar.base_calendar import BaseCalendar

# 创建万年历处理类
bs_calendar = BaseCalendar(app_name="default")  # 可以针对不同app_name创建对应万年历配置
# 判断是否是中国节假日，2004~2023
is_holiday = bs_calendar.is_holiday(datetime.datetime(year=2023, month=10, day=1))
print(f"2023-10-01是否是节假日:{is_holiday}")
