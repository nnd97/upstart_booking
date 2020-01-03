define(function (require) {
    "use strict";
    var $                   = require('jquery'),
        _                   = require('underscore'),
        Gonrin				= require('gonrin');
    
    var template 			= require('text!tpl/location/country/select.html'),
		schema 				= require('json!schema/CountrySchema.json');
    
    return Gonrin.CollectionDialogView.extend({
    	//selectedItems : [],  //[] may be array if multiple selection
    	template : template,
    	modelSchema	: schema,
    	urlPrefix: "/api/v1/",
    	collectionName: "country",
    	//textField: "fullname",
    	tools : [
    	    {
    	    	    	name: "defaultgr",
    	    	    	type: "group",
    	    	    	groupClass: "toolbar-group",
    	    	    	buttons: [
				{
    			    	    	name: "select",
    			    	    	type: "button",
    			    	    	buttonClass: "btn-success btn-sm",
    			    	    	label: "TRANSLATE:SELECT",
    			    	    	command: function(){
    			    	    		var self = this;
    			    	    		self.trigger("onSelected");
    			    	    		self.close();
    			    	    	}
		    	    },
    	    	    	]
    	    },
    	],
    	uiControl:{
    		orderBy:[
	    	    {field: "id",direction:"asc"}
	    	],
	    	fields: [
//	    	     { field: "id", label:"ID", readonly: true },
	     	 { field: "country_name", label: "Country Name" },
	     	 { field: "code", label: "Country Code" }
         ],
         onRowClick: function(event){
	    		this.uiControl.selectedItems = event.selectedItems;
	    	},
    	},
    	render:function(){
    		this.applyBindings();
    	}
    });

});

