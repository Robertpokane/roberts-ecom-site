{"filter":false,"title":"admin.py","tooltip":"/checkout/admin.py","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":12,"column":38},"action":"remove","lines":["from django.contrib import admin","from .models import Order, OrderLineItem","","# Register your models here.","","","class OrderLineAdminInLine(admin.TabularInline):","    model = OrderLineItem","    ","class OrderAdmin(admin.ModelAdmin):","    inlines = (OrderLineAdminInLine, )","    ","admin.site.register(Order, OrderAdmin)"],"id":2},{"start":{"row":0,"column":0},"end":{"row":11,"column":38},"action":"insert","lines":["from django.contrib import admin","from .models import Order, OrderLineItem","","","class OrderLineAdminInline(admin.TabularInline):","    model = OrderLineItem","","","class OrderAdmin(admin.ModelAdmin):","    inlines = (OrderLineAdminInline, )","","admin.site.register(Order, OrderAdmin)"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":11,"column":38},"end":{"row":11,"column":38},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1595106154978,"hash":"4dcede80eec9963f8bfa9506a02e0e9d27640b6d"}