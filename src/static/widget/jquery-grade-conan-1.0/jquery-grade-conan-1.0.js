$(document).ready(function(){ 
	var path = '';
	$('.rating .rate').each(function(idx){
		var v = $(this).attr('v');
		var imgs ='';	

		if($(this).parent().attr('class').indexOf('readonly')==-1){//≈–∂œ÷ª∂¡
			for(i=1;i<=5;i++){
				if(i<=v){
					imgs += '<a href="#'+i+'"><img class="star" s="'+idx+'-'+i+'" src="'+path+'yellow.gif"></a>';
				} else {
					imgs += '<a href="#'+i+'"><img class="star" s="'+idx+'-'+i+'" src="'+path+'gray.gif"></a>';
				}
			}	
		} else {
			for(i=1;i<=5;i++){
				if(i<=v){
					imgs += '<img class="star" s="'+idx+'-'+i+'" src="'+path+'yellow.gif">';
				} else {
					imgs += '<img class="star" s="'+idx+'-'+i+'" src="'+path+'gray.gif">';
				}
			}	
		}
		
		$(this).append(imgs);
		$(this).parent().children('.score').html(v)
		
		$(this).find('a img').each(function(){
			var rateObj = $(this).parent().parent();
			$(this).hover(function(){
				$('#log').html('s='+$(this).attr('s').substr(-1))
				var s= $(this).attr('s').substr(-1);			
				
				rateObj.find('a img').each(function(idx){
					if(idx<s){	
						$(this).attr('src',path+'red.gif');
					} else {
						$(this).attr('src',path+'gray.gif');
					}
					rateObj.parent().children('.score').html(s)
				});
			},function(){
				$('#log').html('v='+$(this).parent().parent().attr('v'))
				var v=rateObj.attr('v')
				rateObj.find('a img').each(function(idx){
					if(idx<v){	
						$(this).attr('src',path+'yellow.gif');
					} else {
						$(this).attr('src',path+'gray.gif');
					}
				});
				rateObj.parent().children('.score').html(v)
			});
			
			$(this).click(function(){
				var s = $(this).attr('s').substr(-1)
				$(this).parent().parent().attr('v',s);
				$(this).parent().parent().parent().children('.score').html(s)
			});		
			
		});
	});
})