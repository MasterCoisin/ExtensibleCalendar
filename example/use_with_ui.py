from extensible_calendar.UI.calendar_ui import CalendarUi
from extensible_calendar.base_calendar.base_calendar import BaseCalendar

# 创建万年历处理类
bs_calendar = BaseCalendar(app_name="default")  # 可以针对不同app_name创建对应万年历配置
# 生成可视化界面进行日期配置
CalendarUi(bs_calendar)