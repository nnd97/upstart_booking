define(function(require) {
	var $          = require("jquery"),
		_          = require("underscore"),
		Gonrin     = require("gonrin"),
		template   = require("text!app/view/port/collection.html"),
		schema 	   = require('json!schema/PortSchema.json');
	
	return Gonrin.CollectionView.extend({
		template: template,
		modelSchema: schema,
		urlPrefix: "/api/",
		collectionName: "port",
		uiControl: {
			orderBy:[
				{ field: "id", direction: "desc" },
				{ field: "port", direction: "asc" },
				{ field: "coupon_prefix", direction: "asc" }
			],
			fields: [
				{ field: "id", label: "ID" },
				{ field: "port", label: "Port" },
				{ field: "server_name", label: "Server" },
				{ field: "coupon_prefix", label: "Coupon" },
				{ field: "tenant_name", label: "Tenant Name" }
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