define(function(require) {
	"use strict";
	
	var $          = require("jquery"),
		_          = require("underscore"),
		Gonrin     = require("gonrin");
	
	var template   = require("text!app/view/port/model.html"),
		schema     = require("json!schema/PortSchema.json");

	return Gonrin.ModelView.extend({
		model: null,
		template: template,
		modelSchema: schema,
		urlPrefix: "/api/",
		collectionName: "port",
		uiControl: {
			fields: [
			]
		},
		
		render: function() {
			const self = this;
			const id = this.getApp().getRouter().getParam("id");
			if (id) {
				this.model.set("id", id);
				this.model.fetch({
					success: function(data) {
						self.applyBindings();
					},
					error: function() {
						self.getApp().notify("Load data error");
					}
				});
			} else {
				self.applyBindings();
			}
		}
	});
})
