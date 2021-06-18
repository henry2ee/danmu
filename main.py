import time
import asyncio
from examples.test_bili_danmu import test_tcp_v2_danmu_client as bi_danmu
from examples.test_huya_danmu import test_ws_danmu_client as hy_danmu
from examples.test_douyu_danmu import test_ws_danmu_client as dy_danmu


# loop.run_until_complete(test_tcp_v2_danmu_client())



print('请选择直播平台 1.B站 2. 虎牙 3. 斗鱼')
platform = int(input())
print('请输入对应平台的房间号码 room id')
room_id = int(input())
loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

if platform == 1:
	loop.run_until_complete(bi_danmu(room_id))
elif platform == 2:
	loop.run_until_complete(hy_danmu(room_id))
elif platform == 3:
	loop.run_until_complete(dy_danmu(room_id))
loop.close()
print('结束，，，请关闭,,,')
time.sleep(100000)
	
	