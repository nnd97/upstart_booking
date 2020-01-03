define(function (require) {
	"use strict";

	var $ = require("jquery"),
		_ = require("underscore"),
		Gonrin = require("gonrin");

	return [
		{
			"text": "Trang chủ",
			"type": "view",
			"collectionName": "index",
			"route": "index",
			"$ref": "app/view/base/IndexView",
			"icon": "fa fa-list-alt"
		},
		{
			"text": "Booking",
			"type": "view",
			"collectionName": "booking",
			"route": "booking/collection",
			"$ref": "app/view/booking/CollectionView",
			"icon": "fa fa-list-alt"
		},
		{
			"type": "view",
			"collectionName": "booking",
			"route": "booking/model(?:id)",
			"$ref": "app/view/booking/ModelView",
			"icon": "fa fa-list-alt",
			"visible": function () {
				return false;
			}
		}
		
		// ,{
		// 	"text": "Location",
		// 	"type": "category",
		// 	"entries": [
		// 		{
		// 			"text": "Country",
		// 			"type": "view",
		// 			"collectionName": "country",
		// 			"route": "country/collection",
		// 			"$ref": "app/view/location/country/CollectionView",
		// 			"icon": "fa fa-list-alt"
		// 		},
		// 		{
		// 			"type": "view",
		// 			"collectionName": "country",
		// 			"route": "country/model(?:id)",
		// 			"$ref": "app/view/location/country/ModelView",
		// 			"icon": "fa fa-list-alt",
		// 			"visible": function () {
		// 				return false;
		// 			}
		// 		},
		// 		{
		// 			"text": "City",
		// 			"type": "view",
		// 			"collectionName": "city",
		// 			"route": "city/collection",
		// 			"$ref": "app/view/location/city/CollectionView",
		// 			"icon": "fa fa-list-alt"
		// 		},
		// 		{
		// 			"type": "view",
		// 			"collectionName": "city",
		// 			"route": "city/model(?:id)",
		// 			"$ref": "app/view/location/city/ModelView",
		// 			"icon": "fa fa-list-alt",
		// 			"visible": function () {
		// 				return false;
		// 			}
		// 		}
		// 	]
		// }
	];
});
