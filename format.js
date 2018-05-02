message เป็น string ที่อาจยาวได้
count คือ string สั้นๆ ไม่น่าเกิน 10 ตัวอักษร
time คือ string {yyyy-mm-dd}T{HH:MM:SS}+0000
pic คือ string url ของรูป
data เอาไว้เก็บ list ของ { } ยกเว้น type99 จะเก็บ 'data':'ขออีกที'
... คือบอกว่ามีเรื่อยๆ (สมาชิกของ list มีหลายตัวมากกว่าที่แสดง)

type = 1
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




