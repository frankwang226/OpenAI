
请求方式：POST（HTTPS）
请求地址：https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token=ACCESS_TOKEN

请求包体：

{
	"userid": "zhangsan",
	"name": "张三",
	"alias": "jackzhang",
	"mobile": "+86 13800000000",
	"department": [1, 2],
	"order":[10,40],
	"position": "产品经理",
	"gender": "1",
	"email": "zhangsan@gzdev.com",
	"biz_mail":"zhangsan@qyycs2.wecom.work",
	"is_leader_in_dept": [1, 0],
	"direct_leader":["lisi"],
	"enable":1,
	"avatar_mediaid": "2-G6nrLmr5EC3MNb_-zL1dDdzkd0p7cNliYu9V5w7o8K0",
	"telephone": "020-123456",
	"address": "广州市海珠区新港中路",
	"main_department": 1,
	"extattr": {
		"attrs": [
			{
				"type": 0,
				"name": "文本名称",
				"text": {
					"value": "文本"
				}
			},
			{
				"type": 1,
				"name": "网页名称",
				"web": {
					"url": "http://www.test.com",
					"title": "标题"
				}
			}
		]
	},
	"to_invite": true,
	"external_position": "高级产品经理",
	"external_profile": {
		"external_corp_name": "企业简称",
		"wechat_channels": {
			"nickname": "视频号名称"
		},
		"external_attr": [
			{
				"type": 0,
				"name": "文本名称",
				"text": {
					"value": "文本"
				}
			},
			{
				"type": 1,
				"name": "网页名称",
				"web": {
					"url": "http://www.test.com",
					"title": "标题"
				}
			},
			{
				"type": 2,
				"name": "测试app",
				"miniprogram": {
					"appid": "wx8bd8012614784fake",
					"pagepath": "/index",
					"title": "my miniprogram"
				}
			}
		]
	}
}
参数说明：

参数	必须	说明
access_token	是	调用接口凭证。获取方法查看“获取access_token”
userid	是	成员UserID。对应管理端的账号，企业内必须唯一。长度为1~64个字节。只能由数字、字母和“_-@.”四种字符组成，且第一个字符必须是数字或字母。系统进行唯一性检查时会忽略大小写。
name	是	成员名称。长度为1~64个utf8字符
alias	否	成员别名。长度1~64个utf8字符
mobile	否	手机号码。企业内必须唯一，mobile/email二者不能同时为空
department	是	成员所属部门id列表，不超过100个
order	否	部门内的排序值，默认为0，成员次序以创建时间从小到大排列。个数必须和参数department的个数一致，数值越大排序越前面。有效的值范围是[0, 2^32)
position	否	职务信息。长度为0~128个字符
gender	否	性别。1表示男性，2表示女性
email	否	邮箱。长度6~64个字节，且为有效的email格式。企业内必须唯一，mobile/email二者不能同时为空
biz_mail	否	企业邮箱。仅对开通企业邮箱的企业有效。长度6~64个字节，且为有效的企业邮箱格式。企业内必须唯一。未填写则系统会为用户生成默认企业邮箱（由系统生成的邮箱可修改一次，2022年4月25日之后创建的成员需通过企业管理后台-协作-邮件-邮箱管理-成员邮箱修改）
telephone	否	座机。32字节以内，由纯数字、“-”、“+”或“,”组成。
is_leader_in_dept	否	个数必须和参数department的个数一致，表示在所在的部门内是否为部门负责人。1表示为部门负责人，0表示非部门负责人。在审批(自建、第三方)等应用里可以用来标识上级审批人
direct_leader	否	直属上级UserID，设置范围为企业内成员，可以设置最多1个上级
avatar_mediaid	否	成员头像的mediaid，通过素材管理接口上传图片获得的mediaid
enable	否	启用/禁用成员。1表示启用成员，0表示禁用成员
extattr	否	自定义字段。自定义字段需要先在WEB管理端添加，见扩展属性添加方法，否则忽略未知属性的赋值。
extattr.type	是	属性类型: 0-文本 1-网页 2-小程序
extattr.name	是	属性名称： 需要先确保在管理端有创建该属性，否则会忽略
extattr.text	否	文本类型的属性
extattr.text.value	是	文本属性内容，长度限制64个UTF8字符
extattr.web	否	网页类型的属性，url和title字段要么同时为空表示清除该属性，要么同时不为空
extattr.web.url	是	网页的url,必须包含http或者https头
extattr.web.title	是	网页的展示标题,长度限制12个UTF8字符
to_invite	否	是否邀请该成员使用企业微信（将通过微信服务通知或短信或邮件下发邀请，每天自动下发一次，最多持续3个工作日），默认值为true。
external_profile	否	成员对外属性，字段详情见对外属性
external_position	否	对外职务，如果设置了该值，则以此作为对外展示的职务，否则以position来展示。长度12个汉字内
nickname	否	视频号名字（设置后，成员将对外展示该视频号）。须从企业绑定到企业微信的视频号中选择，可在“我的企业”页中查看绑定的视频号
address	否	地址。长度最大128个字符
main_department	否	主部门
 

权限说明：

仅通讯录同步助手或第三方通讯录应用可调用。

注意，每个部门下的部门、成员总数不能超过3万个。建议保证创建department对应的部门和创建成员是串行化处理。
返回结果：

{
   "errcode": 0,
   "errmsg": "created"
}
参数说明：

参数	说明
errcode	返回码
errmsg	对返回码的文本描述内容
