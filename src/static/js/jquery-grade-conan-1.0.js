$(document).ready(function(){ 
	var path = 'http://localhost/dota/image/layout/';

	$.getJSON('/heroes/grade/'+hid,function(res){
		update(res);
		
		$('.rating .rate').each(function(idx){
			var v = $(this).attr('v');
			var imgs ='';
			if($(this).parent().attr('class').indexOf('readonly')==-1){//≈–∂œ÷ª∂¡
				for(i=1;i<=5;i++){
					imgs += '<a href="#'+i+'"><img class="star" s="'+idx+'-'+i+'" src="'+path+'gray.gif"></a>';						
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
			$(this).parent().append('<div class="score">'+v+'</div>');
			render($(this));
			
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
				},function(){render(rateObj);
				});
				
				$(this).click(function(){
					var s = $(this).attr('s').substr(-1)
					$(this).parent().parent().attr('v',s);
					$(this).parent().parent().parent().children('.score').html(s)
				});		
				
			});
		});
	});
	
	$('#grade-submit').click(function(){
		var obj = {};
		$('.grade .myGrade .rating .rate').each(function(){
			var name = $(this).attr('name');
			var value = $(this).attr('v');
			obj[name]=value;
		});
		
		$.post('/heroes/grade/'+hid,obj,function(res){
			update(res);
			$('.grade .userGrade .rating .rate').each(function(idx){
				render($(this));
			});
		});
	});
	
	function render(rateObj){
		var v=rateObj.attr('v')
		rateObj.find('img').each(function(idx){
			if(idx<v){	
				$(this).attr('src',path+'yellow.gif');
			} else {
				$(this).attr('src',path+'gray.gif');
			}
		});
		rateObj.parent().children('.score').html(v)
	}
	
	function update(res){
		$('.grade .myGrade .rating .rate').each(function(){
			if($(this).attr('name')=='gank'){$(this).attr('v',res.my.gank)}
			if($(this).attr('name')=='push'){$(this).attr('v',res.my.push)}
			if($(this).attr('name')=='dps'){$(this).attr('v',res.my.dps)}
			if($(this).attr('name')=='assist'){$(this).attr('v',res.my.assist)}
			if($(this).attr('name')=='defend'){$(this).attr('v',res.my.defend)}
		});
		
		$('.grade .userGrade .rating .rate').each(function(){
			if($(this).attr('name')=='gank'){$(this).attr('v',res.user.gank)}
			if($(this).attr('name')=='push'){$(this).attr('v',res.user.push)}
			if($(this).attr('name')=='dps'){$(this).attr('v',res.user.dps)}
			if($(this).attr('name')=='assist'){$(this).attr('v',res.user.assist)}
			if($(this).attr('name')=='defend'){$(this).attr('v',res.user.defend)}
		});
		
		$('.userGrade h4 em').html(res.user.count);
	}
	
})