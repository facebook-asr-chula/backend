message เป็น string ที่อาจยาวได้
count คือ string สั้นๆ ไม่น่าเกิน 10 ตัวอักษร
time คือ string {yyyy-mm-dd}T{HH:MM:SS}+0000
pic คือ string url ของรูป
data เอาไว้เก็บ list ของ { } ยกเว้น type99 จะเก็บ 'data':'ขออีกที'
... คือบอกว่ามีเรื่อยๆ (สมาชิกของ list มีหลายตัวมากกว่าที่แสดง)

**ทุกอันจะมีชื่อกับภาพของเจ้าของเฟสมาด้วย

** พวก เพื่อน เพจ หนังสือ ไรพวกนี้ จะมาพร้อมชื่อและภาพ

***บางอัน อาจจะเห็นว่าใช้แค่อันล่าสุดอันเดียว ซึ่งจริงๆแล้วไม่จำเป็นต้องใช้ list
*** แต่ที่ทำแบบ list ไว้เพราะ เผื่ออยากเปลี่ยนจะได้เปลี่ยนง่าย
***ถ้าอยากเปลี่ยนจำนวนให้เข้าไปแก้ใน backmt.py มันจะมีพวกตัวแปร limit อยู่

**** พวกที่เขียนว่า "มีไม่เกิน" คือเขียนเผื่อไว้ ส่วนมากมันมักจะมีพอดี

type = 1 
			เราโพสอะไร
				แสดงโพสของเรา อันล่าสุดอันเดียว มีข้อความ กับ เวลาโพส
			เราเช็คอินที่ไหน
				แสดงเหมือนโพส แต่ข้อความเป็นสถานที่เช็คอิน อันล่าสุดอันเดียว
ret = 
{
	'type' : 1,
	'sentence' : 'sentence',
	'script' : 'script',
	'name' : 'myname',
	'pic': 'url my pic',
	'data' :
		[
			{
				'message': 'message',
				'time': 'time'
			},
			{
				'message': 'message',
				'time': 'time'
			},
			...
		]
}

type = 2
			โพสต์ล่าสุดมีคนถูกใจกี่คน
				เหมือน เราโพสอะไร แต่มีจำนวนถูกใจเพิ่มเข้ามา
				แสดงโพสของเรา อันล่าสุดอันเดียว มีข้อความ เวลาโพส และจำนวนถูกใจ
			โพสต์ล่าสุดมีคนแชร์กี่คน
				เหมือนอันบน แค่เปลี่ยนไลค์เป็นจำนวนแชร์
ret = 
{
	'type' : 2,
	'sentence' : 'sentence',
	'script' : 'script',
	'name' : 'myname',
	'pic'  : 'url my pic',
	'data' :
		[
			{
				'message': 'message',
				'count': 'count'
			},
			{
				'message': 'message',
				'count': 'count'
			},
			...
		]
}

type = 3
			โพสต์ล่าสุดมีความคิดเห็นอะไร
				แสดงโพสต์ของเราโพสต์ล่าสุด(มีแต่ข้อความ ไม่มีเวลา) กับความคิดเห็นไม่เกิน 5 อัน
				แต่อาจมีไม่ถึง 5 ก็ได้
ret = 
{
	'type' : 3,
	'sentence' : 'sentence',
	'script' : 'script',
	'name' : 'myname',
	'pic'  : 'url my pic',
	'data' :
		[
			{
				'message': 'message',
				'data': 
					[
						{
							'name': 'name',
							'pic': 'url  pic',
							'message': 'message'
						},
						{
							'name': 'name',
							'pic': 'url  pic',
							'message': 'message'
						},
						...
					]
			},
			{
				'message': 'message',
				'data': 
					[
						{
							'name': 'name',
							'pic': 'url  pic',
							'message': 'message'
						},
						{
							'name': 'friend name',
							'pic': 'url  pic',
							'message': 'message'
						},
						...
					]
			}
			...
		]
}

type = 4
			ขอดูเพื่อนของเราหน่อย
				แสดงเพื่อนของเรา 5 คน มีรูปกับชื่อ
			เพจที่เราชอบ
				แสดงเพจที่เราชอบ 5 เพจ มีรูปกับชื่อ
ret = 
{
	'type' : 4,
	'sentence' : 'sentence',
	'script' : 'script',
	'name' : 'myname',
	'pic'  : 'url my pic',
	'data' :
		[
			{
				'name': 'name',
				'pic': 'url  pic'
			},
			{
				'name': 'name',
				'pic': 'url  pic'
			},
			...
		]
}

type = 5
			เพื่อนใช้อะไรเล่นเฟส
				แสดงรูป ชื่อของเพื่อน 5 คนและ os ที่เพื่อนแต่ละใช้เล่นมาไม่เกิน 1 อัน
			ขอจำนวนถูกใจของเพจ
				แสดงรูป ชื่อ เพจ 5 เพจ พร้อมจำนวนไลค์ของแต่ละเพจ
ret = 
{
	'type' : 5,
	'name' : 'myname',
	'pic'  : 'url my pic',
	'data' :
		[
			{
				'name': 'name',
				'pic': 'url  pic',
				'count' : 'count'
			},
			{
				'name': 'friend name',
				'pic': 'url  pic',
				'count' : 'count'
			},
			...
		]
}

type = 6
			ขอดูเพื่อนของเพื่อน
				โชว์เพื่อนของเราคนเดียว และเพื่อนของเพื่อนคนนี้อีกไม่เกิน 5 คน
				โดยทั้งเพื่อน กับ เพื่อนของเพื่อน จะมีทั้งชื่อและภาพ
			ขอดูหนังสือที่เพื่อนชอบ
				โชว์เพื่อนของเรา 5 คน และหนังสือที่เพื่อนชอบคนละไม่เกิน 1 เล่ม
				โดยหนังสือจะมีทั้งชื่อและภาพ
			เพื่อนชอบเพจอะไร
				โชวเพื่อนของเรา 5 คน และเพจที่เพื่อนแต่ละคนชอบ ไม่เกินคนละ 1 เพจ
				ทั้งเพจและเพื่อน จะมีทั้งชื่อและภาพ
ret = 
{
	'type' : 6,
	'name' : 'myname',
	'pic'  : 'url my pic',
	'data' :
		[
			{
				'name': 'name',
				'pic': 'url  pic',
				'data':
					[
						{
							'name': 'name',
							'pic': 'url  pic'
						},
						{
							'name': ' name',
							'pic': 'url  pic'
						},
						...
					]
			},
			{
				'name': ' name',
				'pic': 'url  pic',
				'data':
					[
						{
							'name': 'name',
							'pic': 'url  pic'
						},
						{
							'name': ' name',
							'pic': 'url  pic'
						},
						...
					]
			},
			...
		]
}

type = 7
			เพื่อนโพสต์ว่าอะไร
				โชว์เพื่อน 5 คน กับโพสของแต่ละคน คนละไม่เกิน 1 โพสต์
				โพสมีทั้งข้อความและเวลา
			เพจโพสต์อะไร
				โชว์เพจ 5 เพจ กับโพสของแต่ละเพจไม่เกินเพจละ 1 โพส
				แต่ละโพสมีทั้งข้อความและเวลา
ret = 
{
	'type' : 7,
	'name' : 'myname',
	'pic'  : 'url my pic',
	'data' :
		[
			{
				'name': 'name',
				'pic': 'url  pic',
				'data':
					[
						{
							'message': 'message',
							'time': 'time'
						},
						{
							'message': 'message',
							'time': 'time'
						},
						...
					]
			},
			{
				'name': 'name',
				'pic': 'url  pic',
				'data':
					[
						{
							'message': 'message',
							'time': 'time'
						},
						{
							'message': 'message',
							'time': 'time'
						},
						...
					]
			},
			...
		]
}



type = 99
ret = 
	{
		'type': 99,
		'data': 'ขออีกที'
	}




