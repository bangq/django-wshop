// JavaScript Document
$(function(){
	
	//计算内容上下padding
	reContPadding({main:"#main",header:"#header",footer:"#footer"});
	function reContPadding(o){
		var main = o.main || "#main",
			header = o.header || null,
			footer = o.footer || null;
		var cont_pt = $(header).outerHeight(true),
			cont_pb = $(footer).outerHeight(true);
		$(main).css({paddingTop:cont_pt,paddingBottom:cont_pb});
	}
});
