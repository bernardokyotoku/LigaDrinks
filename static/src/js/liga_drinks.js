odoo.define('liga_drinks.liga_drinks', function (require) {
"use strict";
//techniques for debbuging 
//odoo['order']=this.pos.get_order();

var screens = require('point_of_sale.screens');
var core = require('web.core');
var models = require('point_of_sale.models');

odoo.models = models;
odoo.screens = screens;
var _t = core._t;

screens.PaymentScreenWidget.include({
    template: 'PaymentScreenWidget2',

    renderElement: function() {
        var self = this;
        this._super();
        var receipt = this.pos.get_order().export_for_printing();
        this.$('.print').click(function(){
            self.gui.show_screen('receipt','just_print');
        });
    },

});

screens.ReceiptScreenWidget.include({
    should_close_immediately: function() {
        var self = this;
        var order = this.pos.get_order();
        var params = order.get_screen_data('params');
        order._printed = false;
	if (params == 'just_print'){
          delete order.screen_data['params'];
          self.gui.show_screen('payment');
	  return false;
        } else {
          return this._super();
        };
    },
});

models.Order.prototype.old_export_for_printing = models.Order.prototype.export_for_printing;
models.Order.prototype.export_for_printing = function(){
    var client = this.get_client();
    var receipt = this.old_export_for_printing();
    if (receipt.client) {
         receipt.client = {
             name: client.name,
             phone: client.phone,
             address: client.address,
         };
    };
    return receipt;
};



});


