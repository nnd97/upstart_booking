define(function(require) {
	"use strict";
	
	var $          = require("jquery"),
		_          = require("underscore"),
		Gonrin     = require("gonrin");
	
	var template   = require("text!tpl/location/country/model.html"),
		schema     = require("json!schema/CountrySchema.json");
	
	return Gonrin.ModelView.extend({
		model: null,
		template: template,
		modelSchema: schema,
		urlPrefix: "/api/v1/",
		collectionName: "country",
		uiControl: {
			fields: []
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
						self.getApp().notify(MESSAGE.SYSTEM_ERROR);
					}
				});
			} else {
				self.applyBindings();
			}
		}
	})
})
