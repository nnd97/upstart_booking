define('jquery', [], function () {
    return jQuery;
});

require.config({
    baseUrl: static_url + '/js/lib',
    paths: {
        app: '../app',
        schema: '../schema',
        tpl: '../tpl',
        vendor: '../../vendor'
    },
    shim: {
        'gonrin': {
            deps: ['underscore', 'jquery', 'backbone'],
            exports: 'Gonrin'
        },
        'backbone': {
            deps: ['underscore', 'jquery'],
            exports: 'Backbone'
        },
        'underscore': {
            exports: '_'
        }
    }
});

class Loader {
    show(content = null) {
        if (content) {
            $('body .page-loader-wrapper #loader-content').html(content);
        } else {
            $('body .page-loader-wrapper #loader-content').html("Please wait");
        }
        $('body .page-loader-wrapper').fadeIn();
    }
    hide() {
        $('body .page-loader-wrapper').fadeOut();
        $('body .page-loader-wrapper #loader-content').html("Please wait");
    }
}
window.loader = new Loader();

require([
    'jquery',
    'gonrin',
    'app/router',
    'app/view/base/nav/NavbarView',
    'text!app/view/base/layout.html',
    'i18n!app/nls/app'
], function ($, Gonrin, Router, Nav, layout, lang) {
    $.ajaxSetup({
        headers: {
            "content-type": "application/json"
        }
    });

    var app = new Gonrin.Application({
        router: new Router(),
        lang: lang,
        accountServiceURL: "https://upstart.vn/accounts",
        initialize: function () {
            var self = this;
            var mailEl = $('body .main');
            mailEl.html(layout);
            this.$header = mailEl.find(".page-header");
            this.$content = mailEl.find(".content-area");
            this.$navbar = mailEl.find(".page-navbar");
            this.$toolbox = mailEl.find(".tools-area");

            this.$header.find("#logo").attr("src", static_url + "/images/logo.png");
            // display current username into header bar
            this.$header.find("#header-display-name").html(self.currentUser && self.currentUser.displayname ? self.currentUser.displayname : "Developer");
            this.nav = new Nav({ el: this.$navbar });
            self.nav.render();

            this.router.navigate("/index");
        }
    });
    Backbone.history.start();
});