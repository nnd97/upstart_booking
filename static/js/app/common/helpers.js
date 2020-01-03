define(function(require) {
    "use strict";

    Number.prototype.toRadians = function() { return this * Math.PI / 180; };
    /**
     * ========GET START AND LAST DAY OF ANY MONTH========
     * var startDayOfPeriod = Helper.setDate(2018, 0, 1); // 0: JANUARY
     * var endDayOfPeriod = Helper.setDate(2018, 0 + 1, 0);
     */
    return class Helper {

        constructor() {
            return;
        }

        static nowTimestamp() {
            return moment.now();
        }

        static now_timestamp() {
            return moment.now();
        }

        static now() {
            return moment(new Date()).local();
        }

        static utcNow() {
            return moment(new Date()).utc();
        }

        /**
         * milisecond
         */
        static utcTimestampNow(inputTime = null) {
            var now = moment(new Date()).utc();
            if (inputTime) {
                now = moment(inputTime).utc();
            }
            return now.unix() * 1000 + now.millisecond();
        }


        static datetime(inputTime, inputFormat = null, outputFormat = null) {
            if (inputFormat) {
                if (outputFormat) {
                    return moment(inputTime, inputFormat).format(outputFormat);
                }
                return moment(inputTime, inputFormat);
            } else {
                if (outputFormat) {
                    return moment(inputTime).format(outputFormat);
                }
                return moment(inputTime);
            }
        }

        static localNowString(format = "HH:mm:ss DD-MM-YYYY") {
            return moment(new Date()).local().format(format);
        }

        static utcToLocal(utcTime, format = "HH:mm:ss DD-MM-YYYY") {
            return moment(utcTime).local().format(format);
        }

        static localToUtc(localTime, options = {}) {
            if (!options || !options.format) {
                options.format = "HH:mm:ss DD-MM-YYYY";
            }
            return moment(localTime).utc().format(options.format);
        }

        /**
         *
         * @param {*} utcTime
         * @return miliseconds
         */
        static utcToTimestamp(utcTime, options = {}) {
            let utcMomentTime = this.utcNow();
            if (utcTime) {
                if (options && options.inputFormat) {
                    utcMomentTime = moment().utc(utcTime, options.inputFormat);
                } else {
                    utcMomentTime = moment().utc(utcTime);
                }
            }
            return utcMomentTime.unix() * 1000 + utcMomentTime.millisecond();
        }

        /**
         * convert local time to utc timestamp
         * @param {*} localTime
         * @param {*} options
         */

        static localToUtcTimestamp(localTime, options = {}) {
            let localMomentTime = this.now();
            if (localTime) {
                if (options && options.inputFormat) {
                    localMomentTime = moment(localTime, options.inputFormat);
                } else {
                    localMomentTime = moment(localTime);
                }
            }
            const result = localMomentTime.utc().unix() * 1000 + localMomentTime.millisecond();
            return result;
        }

        /**
         * milisecond
         */
        static datetimeToTimestamp(inputTime = null) {
            var now = moment(new Date());
            if (inputTime) {
                now = moment(inputTime);
            }
            return now.unix() * 1000 + now.millisecond();
        }

        static datetimeToObject(datetime, isUtc = false) {
            try {
                if (!datetime) {
                    datetime = new Date();
                }
                if (moment.isMoment(datetime)) {
                    if (isUtc) {
                        return datetime.local().toObject();
                    } else {
                        return datetime.toObject();
                    }
                } else {
                    if (isUtc) {
                        return moment(datetime).local().toObject();
                    } else {
                        return moment(datetime).toObject();
                    }
                }
            } catch {
                return null;
            }
        }

        static getWeekDayString(idx) {
            var i = parseInt(idx);
            if (i == null) {
                return "";
            }
            switch (i) {
                case 0:
                    return "Chủ nhật";
                case 1:
                    return "Thứ 2";
                case 2:
                    return "Thứ 3";
                case 3:
                    return "Thứ 4";
                case 4:
                    return "Thứ 5";
                case 5:
                    return "Thứ 6";
                case 6:
                    return "Thứ 7";
            }
        }

        static getStartDayTime(inputTime) {
            var t = moment(inputTime);
            t.set('hour', 0);
            t.set('minute', 0);
            t.set('second', 0);
            t.set('millisecond', 0);
            return t;
        }

        static getEndDayTime(inputTime) {
            var t = moment(inputTime);
            t.set('hour', 23);
            t.set('minute', 59);
            t.set('second', 59);
            t.set('millisecond', 999);
            return t;
        }

        static getStartDayOfWeek(currentDay) {
            var first = null;
            if (currentDay.getDay() === 0) {
                first = currentDay.getDate() - 7 + 1;
            } else {
                first = currentDay.getDate() - currentDay.getDay() + 1; // First day is the day of the month - the day of the week
            }
            var firstday = new Date(currentDay.setDate(first)).toUTCString();
            return firstday;
        }

        static getLastDayOfWeek(currentDay) {
            var first = null;
            if (currentDay.getDay() === 0) {
                first = currentDay.getDate() - 7 + 1;
            } else {
                first = currentDay.getDate() - currentDay.getDay() + 1;
            }
            var last = first + 6; // last day is the first day + 6
            var lastday = new Date(currentDay.setDate(last)).toUTCString();
            return lastday;
        }

        static setDate(y = null, m = null, d = null) {
                var today = new Date();
                if (y == null) {
                    y = today.getFullYear();
                }
                if (m == null) {
                    m = today.getMonth();
                } else {
                    m = m - 1;
                }
                if (d == null) {
                    d = today.getDate()
                }
                today.setFullYear(y, m, d);
                return today;
            }
            /**
             * @param {*} value
             */
        static paymentPrediction(value) {
            const maxValue = 1000000000;
            const useageList = [0, 1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000];
            var suggestList = [];
            useageList.forEach(money => {
                var flag = true;
                var i = 0;
                var a = maxValue;
                while (flag && a >= money) {
                    i += 1;
                    var odd = Math.floor(parseFloat(value) % a);

                    var res = value - odd + money;
                    if (!suggestList.includes(res) && res >= value) {
                        suggestList.push(res);
                    }

                    if (Math.floor(parseFloat(value) % a) <= 0) {
                        flag = false;
                    }
                    a = a / 10;
                }
            })
            return suggestList;
        }



        /**
         *
         * @param {*} type
         * @param {*} base
         * @param {*} uppercase
         */
        static generateHashKey(type = "mix", base = 32, uppercase = false) {
            var charsets = null;
            if (type == "number") {
                charsets = "1234567890";
            } else if (type == "string") {
                charsets = "abcdefghijklmnopqrstuvwxyz";
            } else {
                charsets = "abcdefghijklmnopqrs-tuvwxyz1234567890" + "abcdefghijklmnopqrstuvwxyz".toLocaleUpperCase();
            }

            if (uppercase) {
                charsets = charsets.toUpperCase().split("");
            } else {
                charsets = charsets.split("");
            }
            var hash = "";
            var limit = 5;
            var stringDistance = 0;
            if (base >= 16) {
                stringDistance = Math.ceil(base / limit);
            }
            if (stringDistance > 0) {
                for (var i = 0; i < base; i++) {
                    if (i === stringDistance - 1) {
                        hash += "-";
                        stringDistance += Math.ceil(base / limit);
                    }
                    hash += charsets[Math.floor(Math.random() * charsets.length)];
                }
            } else {
                for (var i = 0; i < base; i++) {
                    hash += charsets[Math.floor(Math.random() * charsets.length)];
                }
            }

            return hash;
        }

        /**
         * hex milisecond timestamp to unique string
         */
        static toHexTimestamp() {
            var input = this.datetimeToTimestamp();
            var alphabet = "0123456789abcdefghijklmnopqrstuvwxyz" + "abcdefghijklmnopqrstuvwxyz".toLocaleUpperCase();
            var hashids = new Hashids(alphabet);
            var id = hashids.encode(input);
            return id;
        }

        /**
         * generate uniqueId base on timestamp by milisecond
         */
        static uniqueId() {
            var input = this.now_timestamp();
            var hash = "",
                alphabet = "0123456789abcdefghijklmnopqrstuvwxyz".toLocaleUpperCase(),
                alphabetLength = alphabet.length;
            do {
                hash = alphabet[input % alphabetLength] + hash;
                input = parseInt(input / alphabetLength, 10);
            } while (input);
            return hash + alphabet.charAt(Math.floor(Math.random() * alphabet.length));
        }

        static validatePhone(inputPhone) {
                var phoneno = /(09|08|07|05|03)+[0-9]{8}/g;
                const result = inputPhone.match(phoneno);
                if (result && result == inputPhone) {
                    return true;
                } else {
                    return false;
                }
            }
            /**
             *
             * @param {*} previousItems: itemA
             * @param {*} newItems: itemB
             */

        static getDifferentItemPath(previousItems = [], newItems = []) {
            var arrayA = clone(previousItems); // original array
            var arrayB = clone(newItems); // new array
            // FIND NEW ADDED

            var newAddedItems = [];
            var newScannedItems = [];

            function newOrderAction(item) {
                var newItem = clone(item);
                if (newItem.notify_to && !newScannedItems.includes(newItem.notify_to._id)) {
                    newScannedItems.push(newItem.notify_to._id);
                    newAddedItems.push({
                        area_id: newItem.notify_to._id,
                        area_name: newItem.notify_to.area_name,
                        items: [newItem]
                    });
                } else if (newItem.notify_to && newScannedItems.includes(newItem.notify_to._id)) {
                    newAddedItems.forEach(x => {
                        if (x.area_id == newItem.notify_to._id) {
                            x.items.push(newItem);
                        }
                    });
                }
            }

            var releasedItems = [];
            var releaseScannedItems = [];

            function releaseOrderAction(item) {
                var releaseItem = clone(item);
                if (releaseItem.notify_to && !releaseScannedItems.includes(releaseItem.notify_to._id)) {
                    releaseScannedItems.push(releaseItem.notify_to._id);
                    releasedItems.push({
                        area_id: releaseItem.notify_to._id,
                        area_name: releaseItem.notify_to.area_name,
                        items: [releaseItem]
                    });
                } else if (releaseItem.notify_to && releaseScannedItems.includes(releaseItem.notify_to._id)) {
                    releasedItems.forEach(x => {
                        if (x.area_id == releaseItem.notify_to._id) {
                            x.items.push(releaseItem);
                        }
                    });
                }
            }

            var newComboItems = [];
            var releaseComboItems = [];
            arrayB.forEach(itemB => {
                var newComboItem = clone(itemB);
                var exist = false;
                arrayA.forEach(itemA => {
                    if (itemA._id == itemB._id && itemA.product_type != "product" && itemB.product_type != "product") {
                        if (itemB.quantity > itemA.quantity) {
                            newComboItem.quantity = itemB.quantity - itemA.quantity;
                            newComboItems.push(newComboItem);
                        }
                        exist = true;
                    }
                });
                if (!exist) {
                    if (itemB.product_type != "product") {
                        newComboItems.push(newComboItem)
                    }
                }
            });

            // FIND RELEASED ITEMS
            arrayA.forEach(itemA => {
                var exist = false;
                var releasedComboItem = clone(itemA);
                arrayB.forEach(itemB => {
                    if (itemB._id == itemA._id && itemA.product_type != "product" && itemB.product_type != "product") {
                        if (itemA.quantity > itemB.quantity) {
                            releasedComboItem.quantity = itemA.quantity - itemB.quantity;
                            releaseComboItems.push(releasedComboItem);
                        }
                        exist = true;
                    }
                });
                if (!exist) {
                    if (itemA.product_type != "product") {
                        releaseComboItems.push(releasedComboItem);
                    }
                }
            });

            var packageItemsA = [];
            var packageItemsB = [];
            //check each item of previousItems
            releaseComboItems.forEach(itemA => {
                if (itemA.product_type != "product") {
                    if (itemA.package_products) {
                        itemA.package_products.forEach((pkgItem, idx) => {
                            // GENERATE NEW ID TO MAKE SURE THIS ITEM GO TO MADE AREA
                            pkgItem.id = gonrin.uuid();
                            pkgItem.quantity = pkgItem.quantity * itemA.quantity;
                            pkgItem.product_name = pkgItem.product_name + " (" + itemA.product_no + ")";
                            pkgItem.note = itemA.note ? itemA.note : "";
                            packageItemsA.push(pkgItem);
                        })
                    }
                }
            });

            newComboItems.forEach(itemB => {
                if (itemB.product_type != "product") {
                    if (itemB.package_products) {
                        itemB.package_products.forEach((pkgItem, idx) => {
                            // GENERATE NEW ID TO MAKE SURE THIS ITEM GO TO MADE AREA
                            pkgItem.id = gonrin.uuid();
                            pkgItem.quantity = pkgItem.quantity * itemB.quantity;
                            pkgItem.product_name = pkgItem.product_name + " (" + itemB.product_no + ")";
                            pkgItem.note = itemB.note ? itemB.note : "";
                            packageItemsB.push(pkgItem);
                        })
                    }
                }
            });

            arrayA = arrayA.concat(packageItemsA);
            arrayA = lodash.orderBy(arrayA, ['product_name'], ['asc']);
            // FIND RELEASED ITEMS
            arrayA.forEach(itemA => {
                var exist = false;
                var releasedItem = clone(itemA);
                arrayB.forEach(itemB => {
                    if (itemB._id == itemA._id) {
                        if (itemA.quantity > itemB.quantity && itemA.product_type == "product" && itemB.product_type == "product") {
                            releasedItem.quantity = itemA.quantity - itemB.quantity;
                            releaseOrderAction(releasedItem);
                        }
                        exist = true;
                    }
                });
                if (!exist) {
                    if (releasedItem.product_type == "product") {
                        releaseOrderAction(releasedItem);
                    }
                }
            });

            arrayB = arrayB.concat(packageItemsB);
            arrayB = lodash.orderBy(arrayB, ['product_name'], ['asc']);
            arrayB.forEach(itemB => {
                var newAdded = clone(itemB);
                var exist = false;
                arrayA.forEach(itemA => {
                    if (itemA._id == itemB._id && itemA.product_type == "product" && itemB.product_type == "product") {
                        if (itemB.quantity > itemA.quantity) {
                            newAdded.quantity = itemB.quantity - itemA.quantity;
                            newOrderAction(newAdded)
                        }
                        exist = true;
                    }
                });
                if (!exist) {
                    if (newAdded.product_type == "product") {
                        newOrderAction(newAdded);
                    }
                }
            });

            return {
                'newAddedItems': newAddedItems,
                'releasedItems': releasedItems
            };
        }

        /**
         *
         * @param {*} salesorderproducts
         */
        static mergeSalesorderProducts(salesorderproducts) {
            // GROUP ORDERED PRODUCT BY QUANTITY
            var list_items = JSON.parse(JSON.stringify(salesorderproducts));
            let loadedProducts = [];
            var salesorderProductGroup = [];
            if (list_items) {
                list_items.forEach((item, idx) => {
                    if (!loadedProducts.includes(item.product_no)) {
                        loadedProducts.push(item.product_no);
                        let holdItem = clone(item);
                        for (let i = idx + 1; i < salesorderproducts.length; i++) {
                            if (holdItem.product_no == salesorderproducts[i].product_no) {
                                holdItem.quantity += salesorderproducts[i].quantity;
                                holdItem.net_amount += salesorderproducts[i].net_amount;
                                holdItem.amount += salesorderproducts[i].amount;
                                holdItem.discount_amount += salesorderproducts[i].discount_amount;
                                holdItem.discount_percent += holdItem.discount_amount / holdItem.net_amount;
                            }
                        }
                        salesorderProductGroup.push(holdItem);
                    }
                })
            }
            return salesorderProductGroup;
        }


        /**
         * FILE EXPORT AS EXCEL
         * @param {*} title
         * @param {*} dataSource
         * @param {*} fields
         */
        static exportToFile(title = null, dataSource, fields) {
            // try {
            const self = this;
            if (!title) {
                title = self.localNowString("YYYY-MM-DD-HH-mm-ss");
            } else {
                title += "-" + self.localNowString("YYYY-MM-DD-HH-mm-ss");
            }

            var report = gonrin.spreadsheet({
                name: title,
                fields: fields,
                dataSource: dataSource,
                excel: {
                    file_name: title + ".xlsx"
                }
            }).save_excel();

            var createFile = function(workbook, options) {
                var zip = new JSZip();
                var files = workbook.generateFiles();
                $.each(files, function(path, content) {
                    path = path.substr(1);
                    if (path.indexOf('.xml') !== -1 || path.indexOf('.rel') !== -1) {
                        zip.file(path, content, {
                            base64: false
                        });
                    } else {
                        zip.file(path, content, {
                            base64: true,
                            binary: true
                        });
                    }
                })
                options = options || {};
                if (!options.type) {
                    options.type = "base64";
                }
                return zip.generate(options);
            };

            var rhref = createFile(report.prepare());

            $("#download").attr({
                href: "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64," + rhref
            });
            // } catch (error) {
            //     $.notify({message: error}, {type: "danger"});
            // }
        }


        static objectExtend(obj, src) {
            Object.keys(src).forEach(function(key) { obj[key] = src[key]; });
            return obj;
        }

        static distance(lat1, lon1, lat2, lon2, unit) {
            if ((lat1 == lat2) && (lon1 == lon2)) {
                return 0;
            } else {
                // var radlat1 = Math.PI * lat1/180;
                // var radlat2 = Math.PI * lat2/180;
                // var theta = lon1-lon2;
                // var radtheta = Math.PI * theta/180;
                // var dist = Math.sin(radlat1) * Math.sin(radlat2) + Math.cos(radlat1) * Math.cos(radlat2) * Math.cos(radtheta);
                // if (dist > 1) {
                //     dist = 1;
                // }
                // dist = Math.acos(dist);
                // dist = dist * 180/Math.PI;
                // dist = dist * 60 * 1.1515;
                // if (unit=="K") {
                //     dist = dist * 1.609344
                // }
                // if (unit=="N") {
                //     dist = dist * 0.8684
                // }
                // return dist;

                var R = 6371e3; // metres
                var x1 = lat1.toRadians();
                var x2 = lat2.toRadians();
                var delta1 = (lat2 - lat1).toRadians();
                var delta2 = (lon2 - lon1).toRadians();

                var a = Math.sin(delta1 / 2) * Math.sin(delta1 / 2) +
                    Math.cos(x1) * Math.cos(x2) *
                    Math.sin(delta2 / 2) * Math.sin(delta2 / 2);
                var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

                var d = R * c;
                return d;
            }
        }

        static QRCodeScanner(successCallback, errorCallback) {

            cordova.plugins.barcodeScanner.scan(
                function(result) {
                    // alert("We got a barcode\n" +
                    // 	"Result: " + result.text + "\n" +
                    // 	"Format: " + result.format + "\n" +
                    // 	"Cancelled: " + result.cancelled);
                    successCallback(result);
                },
                function(error) {
                    errorCallback(error);
                }, {
                    preferFrontCamera: true, // iOS and Android
                    showFlipCameraButton: true, // iOS and Android
                    showTorchButton: true, // iOS and Android
                    torchOn: true, // Android, launch with the torch switched on (if available)
                    saveHistory: false, // Android, save scan history (default false)
                    prompt: "Đặt mã vạch bên trong khu vực quét", // Android: Place a barcode inside the scan area
                    resultDisplayDuration: 0, // Android, display scanned text for X ms. 0 suppresses it entirely, default 1500
                    formats: "QR_CODE,PDF_417", // default: all but PDF_417 and RSS_EXPANDED
                    orientation: "portrait", // Android only (portrait|landscape), default unset so it rotates with the device
                    disableAnimations: true, // iOS
                    disableSuccessBeep: false // iOS and Android
                }
            );
        }

        static removeAccents(str) {
            var AccentsMap = [
                "aàảãáạăằẳẵắặâầẩẫấậ",
                "AÀẢÃÁẠĂẰẲẴẮẶÂẦẨẪẤẬ",
                "dđ", "DĐ",
                "eèẻẽéẹêềểễếệ",
                "EÈẺẼÉẸÊỀỂỄẾỆ",
                "iìỉĩíị",
                "IÌỈĨÍỊ",
                "oòỏõóọôồổỗốộơờởỡớợ",
                "OÒỎÕÓỌÔỒỔỖỐỘƠỜỞỠỚỢ",
                "uùủũúụưừửữứự",
                "UÙỦŨÚỤƯỪỬỮỨỰ",
                "yỳỷỹýỵ",
                "YỲỶỸÝỴ"
            ];
            for (var i = 0; i < AccentsMap.length; i++) {
                var re = new RegExp('[' + AccentsMap[i].substr(1) + ']', 'g');
                var char = AccentsMap[i][0];
                str = str.replace(re, char);
            }
            return str;
        }

        static formatMoney(number) {
            return new Intl.NumberFormat("vi-VN").format(number);
        }

        static formatMoneyCompact(number) {
            // return new Intl.NumberFormat("vi-VN").format(number);
            let result = "";
            if (number >= 1000) {
                number = (number / 1000);
                result = String(number) + "K"
            }
            return result;
        }

    }
});