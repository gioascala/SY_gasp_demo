odoo.define('tree_menu.tree_view_button', function (require){
"use strict";

var core = require('web.core');
var ListView = require('web.ListView');
var QWeb = core.qweb;

ListView.include({

        render_buttons: function($node) {
                var self = this;
                this._super($node);
                    this.$buttons.find('.o_list_tender_button_create').click(this.proxy('tree_view_action'));
                            console.log("asd");

        },

        tree_view_action: function () {
        console.log("asd2");
        this.do_action({
                type: "ir.actions.act_window",
                name: "l4_live_streaming",
                res_model: "syenmaint.l4_live_streaming",
                views: [[false,'form']],
                target: 'current',
                view_type : 'form',
                view_mode : 'form',
                flags: {'form': {'action_buttons': true, 'options': {'mode': 'edit'}}}

        });
        console.log("this.res_model");
        return { 'type': 'ir.actions.client','tag': 'reload', } }

});

});