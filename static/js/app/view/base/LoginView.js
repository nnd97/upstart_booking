define(function(require) {
	"use strict";
	
	var $          = require("jquery"),
		_          = require("underscore"),
		Gonrin     = require("gonrin"),
		tpl        = require("text!./tpl/login.html"),
		template   = _.template(tpl);
		
	return Gonrin.View.extend({
		render: function() {
			var self = this;
			this.$el.html(template());
			
			this.$el.find("#login-form").unbind("submit").bind("submit", function() {
				self.processLogin();
				return false;
			})
			return this;
		},
		
		processLogin: function() {
			const username = this.$el.find('[name=username]').val();
			const password = this.$el.find('[name=password]').val();
			const data = JSON.stringify({
   		        username: username,
   		        password: password
   		    });
			
			var self = this;
			$.ajax({
				url: self.getApp().serviceURL + "/login",
				type: "post",
				data: data,
				headers: {
       		    	'content-type': 'application/json'
       		    },
       		    dataType: 'json',
				success: function(data) {
					self.getApp().postLogin(data);
				},
				error: function(XMLHttpRequest, textStatus, errorThrown) {
					self.getApp().notify("Login error");
				}
			})
		}
	});
		
	
});