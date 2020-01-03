define(function(require) {
	"use strict";
	
	var $          = require("jquery"),
		_          = require("underscore"),
		Gonrin     = require("gonrin");
	
	var template   = require("text!tpl/location/city/model.html"),
		schema     = require("json!schema/CitySchema.json");
	
	var CountrySelectView = require("app/view/location/country/SelectView");

	return Gonrin.ModelView.extend({
		model: null,
		template: template,
		modelSchema: schema,
		urlPrefix: "/api/v1/",
		collectionName: "city",
		uiControl: {
			fields: [
				{
					field: "country",
					textField: "country_name",
					uicontrol: "ref",
					selectionMode: "single",
					dataSource: CountrySelectView
				}
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
						self.getApp().notify(MESSAGE.SYSTEM_ERROR);
					}
				});
			} else {
				self.applyBindings();
			}
		}
	});
})
