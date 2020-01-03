define(function(require) {
	"use strict";
	
	var $           = require('jquery'),
		_           = require('underscore'),
    		Gonrin    	= require('gonrin');
    
	var IndexView  = require('app/view/base/IndexView');
		
	return Gonrin.Router.extend({
		routes: {
			"index": "index",
//			"login": "login",
//			"logout": "logout",
			"error": "error_page",
			"*path": "defaultRoute"
		},
		
		index: function() {
			var indexView = new IndexView({el: $("body")});
			indexView.render();
		},
		
//		login: function() {
//			var loginView = new Login({el: $("body")});
//			loginView.render();
//		},
		
//		logout: function() {
//        	var self = this;
//        	$.ajax({
//				url: self.getApp().serviceURL + '/logout',
//       		    dataType:"json",
//       		    success: function (data) {
//       		    		self.navigate("login");
//       		    		return;
//       		    },
//       		    error: function(XMLHttpRequest, textStatus, errorThrown) {
//       		    		self.getApp().notify(self.getApp().translate("Lỗi hệ thống, thử lại sau!"));
//       		    }
//        	});
//        },
		
		error_page: function() {
			var app = this.getApp();
			if (app.$content) {
				app.$content.html("Error Page");
			}
		},
		
		defaultRoute: function() {
        		this.navigate("index", true);
        },
	});
})