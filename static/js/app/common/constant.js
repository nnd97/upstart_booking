define(function() {
	return {
		GENDER_LIST: [
			{ "text": "Nam", "value": "nam" },
			{ "text": "Nữ", "value": "nu" }
		],
		YES_NO_LIST: [
			{ "text": "Có", "value": true },
			{ "text": "Không", "value": false }
		],
		ACTIVE_STATUS_LIST: [
			{ text: "Hoạt động", value: true },
			{ text: "Khoá", value: false }
		],
		SUBJECT_LIST: [
			{
				"text": "Thông tin hành chính",
				"value": "tt-hanh-chinh",
				"entities": ["user", "hoten", "sodienthoai", "email", "ngaysinh", "gioitinh", "tolop", "nam", "tiensu"]
			},
			{
				"text": "Thể lực",
				"value": "the-luc",
				"entities": ["chieucao", "cannang", "vongnguctrungbinh"]
			},
			{
				"text": "Da liễu",
				"value": "da-lieu",
				"entities": ["dalieu"]
			},
			{
				"text": "Thị lực",
				"value": "thi-luc",
				"entities": ["cokinh", "mattrai", "matphai"]
			},
			{
				"text": "Tai mũi họng",
				"value": "tai-mui-hong",
				"entities": ["taimuihong"]
			},
			{
				"text": "Huyết áp",
				"value": "huyet-ap",
				"entities": ["huyetap_toida", "huyetap_toithieu"]
			},
			{
				"text": "Răng hàm mặt",
				"value": "rang-ham-mat",
				"entities": ["ranghammat"]
			},
			{
				"text": "Nội khoa",
				"value": "noi-khoa",
				"entities": ["noikhoa"]
			},
			{
				"text": "Mắt",
				"value": "mat",
				"entities": ["mat"]
			},
			{
				"text": "Kết luận",
				"value": "ket-luan",
				"entities": ["ketluan"]
			}
		],
		
		PERMISSION_LIST: [
			{ "text": "Đọc", "value": "read", "subject": "tt-hanh-chinh" },
			{ "text": "Ghi", "value": "write", "subject": "tt-hanh-chinh" }
		]
	}
})
