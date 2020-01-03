define(function(require) {
	var $          = require("jquery"),
		_          = require("underscore"),
		Gonrin     = require("gonrin"),
		template   = require("text!tpl/location/city/collection.html"),
		schema 	   = require('json!schema/CitySchema.json');
	
	return Gonrin.CollectionView.extend({
		template: template,
		modelSchema: schema,
		urlPrefix: "/api/v1/",
		collectionName: "city",
		uiControl: {
			orderBy:[ {field: "created_at",direction: "asc"}],
			fields: [
				{ field: "id", label: "ID", width: "250px" },
				{ field: "city_name", label: "City Name" },
				{ field: "code", label: "code" },
				{ field: "country", label: "Country Name", template: function(row) {
					return row.country.country_name ? row.country.country_name : "";
				}},
				{ field: "created_at", label: "Created Date" }
		    ],
		    onRowClick: function(event) {
		    		if (event.rowId) {
		    			// http://.../city/model?id=123
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