define(function(require) {
	var $          = require("jquery"),
		_          = require("underscore"),
		Gonrin     = require("gonrin"),
		template   = require("text!tpl/location/country/collection.html"),
		schema 	   = require('json!schema/CountrySchema.json');
	
	return Gonrin.CollectionView.extend({
		template: template,
		modelSchema: schema,
		urlPrefix: "/api/v1/",
		collectionName: "country",
		uiControl: {
			orderBy:[ {field: "created_at",direction: "asc" }],
			fields: [
				{ field: "id", label: "ID", width: "250px" },
				{ field: "country_name", label: "Country Name" },
				{ field: "code", label: "code" },
				{ field: "created_at", label: "Created Date" }
		    ],
		    onRowClick: function(event) {
		    		if (event.rowId) {
		    			// http://.../country/model?id=123
		    			var path = this.collectionName + '/model?id=' + event.rowId;
		        		this.getApp().getRouter().navigate(path);
	    			}
		    }
		},
		render: function() {
	    	 	this.applyBindings();
	    	 	return this;
		}
	})
})