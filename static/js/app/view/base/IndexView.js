define(function(require) {
    "use strict";

    var $ = require("jquery"),
        _ = require("underscore"),
        Gonrin = require("gonrin"),
        tpl = require("text!tpl/base/index.html"),
        template = _.template(tpl);

    var Helper = require('app/common/helpers');

    return Gonrin.View.extend({
        render: function() {
            this.$el.html(template());
            this.registerEvent();
            this.getListInfoAccountToday();
            this.todayWeekMonthWithUser();
            return this;
        },

        registerEvent: function() {
            const self = this;

            // self.$el.find('#to-datetime').datetimepicker({
            //     format: "DD/MM/YYYY HH:mm",
            //     icons: {
            //         time: "fa fa-clock"
            //     }
            // });
        },

        getListInfoAccountToday: function() {
            const self = this;
            var TODAY = new Date();
            var startUtcTimestamp = 1568480400 * 1000;
            var endUtcTimestamp = Helper.datetimeToTimestamp(Helper.getEndDayTime(TODAY));
            self.loadListInfoAccount(startUtcTimestamp, endUtcTimestamp);

            self.loadTenant(startUtcTimestamp, endUtcTimestamp);
        },

        loadListInfoAccount: function(startUtcTimestamp, endUtcTimestamp) {
            const self = this;
            $.ajax({
                type: "POST",
                url: self.getApp().accountServiceURL + "/api/user/get_list_info",
                data: JSON.stringify({
                    form_timestamp: startUtcTimestamp,
                    to_timestamp: endUtcTimestamp,
                }),
                success: function(response) {
                    self.renderGrid(response);
                    self.$el.find("#total").text(response.length);
                },
                error: function(error) {
                    console.log("error", error);
                }
            });
        },

        todayWeekMonthWithUser: function() {
            const self = this;
            var TODAY = new Date();
            var startUtcTimestamp = Helper.datetimeToTimestamp(Helper.getStartDayTime(TODAY));
            var endUtcTimestamp = Helper.datetimeToTimestamp(Helper.getEndDayTime(TODAY));


            // WEEK
            var firstDay = Helper.getStartDayOfWeek(TODAY);
            var lastDay = Helper.getLastDayOfWeek(TODAY);
            var startUtcTimestampWeek = Helper.datetimeToTimestamp(Helper.getStartDayTime(firstDay));
            var endUtcTimestampWeek = Helper.datetimeToTimestamp(Helper.getEndDayTime(lastDay));

            // month
            var startDayOfPeriod = Helper.setDate(null, TODAY.getMonth() + 1, 1);
            var endDayOfPeriod = Helper.setDate(null, TODAY.getMonth() + 2, 0);
            var startUtcTimestampMonth = Helper.datetimeToTimestamp(Helper.getStartDayTime(startDayOfPeriod));
            var endUtcTimestampMonth = Helper.datetimeToTimestamp(Helper.getEndDayTime(endDayOfPeriod));


            $.ajax({
                type: "POST",
                url: self.getApp().accountServiceURL + "/api/user/get_list_info",
                data: JSON.stringify({
                    form_timestamp: startUtcTimestamp,
                    to_timestamp: endUtcTimestamp,
                }),
                success: function(response) {
                    self.$el.find("#today").text(response.length);
                },
                error: function(error) {
                    console.log("error", error);
                }
            });

            $.ajax({
                type: "POST",
                url: self.getApp().accountServiceURL + "/api/user/get_list_info",
                data: JSON.stringify({
                    form_timestamp: startUtcTimestampWeek,
                    to_timestamp: endUtcTimestampWeek,
                }),
                success: function(response) {
                    self.$el.find("#week").text(response.length);
                },
                error: function(error) {
                    console.log("error", error);
                }
            });


            $.ajax({
                type: "POST",
                url: self.getApp().accountServiceURL + "/api/user/get_list_info",
                data: JSON.stringify({
                    form_timestamp: startUtcTimestampMonth,
                    to_timestamp: endUtcTimestampMonth,
                }),
                success: function(response) {
                    self.$el.find("#month").text(response.length);
                },
                error: function(error) {
                    console.log("error", error);
                }
            });
        },

        renderGrid: function(data) {
            const self = this;
            self.$el.find("#list-account").grid({
                pagination: {
                    page: 1,
                    pageSize: 50
                },
                refresh: true,
                orderBy: [{
                    field: "created_at",
                    direction: "desc"
                }],
                fields: [{
                        field: "display_name",
                        label: "Tên hiểu thị",
                    },
                    {
                        field: "email",
                        label: "Email"
                    },
                    {
                        field: "phone",
                        label: "Phone",
                    },
                    {
                        field: "created_at",
                        label: "Ngày tạo",
                        template: function(rowObject) {
                            return `<div class="text-left ellipsis-200">${Helper.utcToLocal(rowObject.created_at, "YYYY-MM-DD HH:mm")}</div>`;
                        }
                    },
                    {
                        field: "active",
                        lable: "Trạng thái",
                        template: function(rowObject) {
                            if (rowObject.active && rowObject.active == true) {
                                return `<div style="color: #4cae4c;" >Đang hoạt động</div>`;
                            } else {
                                return `<div>Không hoạt động</div>`;
                            }
                        }
                    },
                ],
                dataSource: data,
                onRendered: function(event) {}
            })
        },

        loadTenant: function(fromDate, toDate) {
            const self = this;

            $.ajax({
                type: "POST",
                url: "https://upstart.vn/accounts/api/v1/tenant/get_list_info",
                data: JSON.stringify({
                    form_timestamp: fromDate,
                    to_timestamp: toDate
                }),
                success: function(response) {
                    if (response) {
                        self.$el.find("#total_tenant").text(response.length);
                        let businessLine = response.filter(r => r.business_line != null);
                        self.$el.find("#business_line").text(businessLine.length);

                    }
                    self.$el.find("#list-tenant").grid({
                        pagination: {
                            page: 1,
                            pageSize: 50
                        },
                        refresh: true,
                        orderBy: [{
                            field: "created_at",
                            direction: "desc"
                        }],
                        fields: [{
                                field: "tenant_name",
                                label: "Thương hiệu"
                            },
                            {
                                field: "image_url",
                                label: "Hình ảnh",
                                template: (rowData) => {
                                    return `<img src="${rowData.image_url}}" style="height: 80px; width: 80px">`;
                                }
                            },
                            {
                                field: "created_at",
                                label: "Ngày tạo",
                                template: function(rowObject) {
                                    return `<div class="text-left ellipsis-200">${Helper.utcToLocal(rowObject.created_at, "YYYY-MM-DD HH:mm")}</div>`;
                                }
                            },
                            {
                                field: "business_line",
                                label: "Dữ liệu mặc định"
                            },
                            {
                                field: "active",
                                lable: "Trạng thái",
                                template: function(rowObject) {
                                    if (rowObject.active && rowObject.active == true) {
                                        return `<div style="color: #4cae4c;" >Đang hoạt động</div>`;
                                    } else {
                                        return `<div>Không hoạt động</div>`;
                                    }
                                }
                            },
                        ],
                        dataSource: response,
                        onRendered: function(event) {}
                    })
                }
            });
        },
    })
})