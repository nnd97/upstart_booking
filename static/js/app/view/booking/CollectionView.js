define(function(require) {
	var $          = require("jquery"),
		_          = require("underscore"),
		Gonrin     = require("gonrin"),
        template   = require("text!./tpl/collection.html"),
		schema     = require("json!schema/BookingSchema.json");

	var Helpers = require('app/common/Helpers');
	
	return Gonrin.CollectionView.extend({
		template: template,
		modelSchema: schema,
		urlPrefix: "/api/",
		collectionName: "booking",
		uiControl: {
			orderBy:[
				{ field: "date", direction: "desc"}
			], 
			fields: [
				{
					field: "phone",
					label: "Phone"
				},
				{ 	
					field: "date",
					label: "Date", 
					cssClass: "text-center",
					template: function(rowObject) {
						if (rowObject.date) {
							try {
								return Helpers.setDatetime(rowObject.date, { format: 'DD/MM/YYYY THH:mm' });
							} catch (error) {
								return '';
							}
						}
						return '';
					}
				},
				{ field: "slot", label: "Slot"},
				{ field: "note", label: "Note"}
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