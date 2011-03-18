var _d = document;
function $(name) {
	return _d.getElementById(name);
}
function Tutorial(obj,list){
	var div_s = $('Tutorial').getElementsByTagName("div");
	var h3_s = $('Tutorial').getElementsByTagName("h3");
	var n = 0;
	for (var i = 0 ; i < div_s.length; i ++){
		if(div_s[i].className == "box"){n++;div_s[i].style.display = "none";}
		if(n == list){div_s[i].style.display = "";}
		if(h3_s[i].className == "title Tuyes_title"){h3_s[i].className = "title Tuno_title"}
	}
	obj.className = "title Tuyes_title";
}
function Display(obj,id){
	var lis = $("menu").getElementsByTagName("li");
	for(var i = 0 ; i < lis.length; i++){
		if(i != obj){lis[i].className = "";}else{lis[i].className = "menu_hover";}
	}
	var div_s = $("box").getElementsByTagName("div");
	for(var j = 0; j < div_s.length; j++){
		if(div_s[j].className == "Skills" || div_s[j].className == "Routine"){div_s[j].style.display = "none";}
		if(div_s[j].className == id){div_s[j].style.display = "";}
	}
}
var show_part = new Array();
var show_title = new Array();
function showpart(obj,showid,n) {
	if (show_part[n]) show_part[n].style.display = "none";
	if (show_title[n]) show_title[n].className = "txt_3";
	obj.className = "txt_3_1";
	show_part[n] = document.getElementById(showid);
	show_part[n].style.display = "block";
	show_title[n] = obj;
}
function Img_Nav(u){
	var ulid = "navimg" + u;
	if($(ulid).style.display == ""){
		$(ulid).style.display = "none";
	}else{
		$(ulid).style.display = "";
	}
}
var  showpartt;
function showcomment(id){
	var divs = $("dotaerp").getElementsByTagName("div");
	var divid = "comment_" + id;
	if (showpartt)$(showpartt).style.display = "none";
	$(divid).style.display = "block";
	showpartt = divid;
	$(divid).onclick = function(){this.style.display="none"};
}
function bookmark(title, url){
if (document.all) {window.external.AddFavorite(url, title)}
else {if (window.sidebar) window.sidebar.addPanel(title, url, "")}
}


