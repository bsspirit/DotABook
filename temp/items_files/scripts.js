var noTime;
function showNotif(hide)
{

	if (hide == 2)
	{
		clearTimeout(noTime);
		return;
	}

	if (noTime) clearTimeout(noTime);
	if (hide == 1)
	{
		clearTimeout(noTime);
		noTime = setTimeout(
		function()
		{
			$('notifications_menu').hide();
		}, 500 );
		return;
	}


	if ($('notifications_menu').getStyle('display') == 'none')
	{
		var curleft = 0;
		var curtop = 0;
		obj = $('shNotif');

		if (obj.offsetParent) {
			do {
				curleft += obj.offsetLeft;
				curtop += obj.offsetTop;
			} while (obj = obj.offsetParent);
		}
		$('notifications_menu').style.display = '';

	} else $('notifications_menu').hide();

}

function gType(val)
{
(val == 1)?document.getElementById('hList').style.display='':document.getElementById('hList').style.display='none';
}
function addLevel(lev)
{
	curLevel[lev]++;
	var ob = document.getElementById("levels-"+lev);
	var objDiv = document.createElement("div");
	objDiv.innerHTML += '<ul class="l"><li style="width:50px;"><input type="text" size="2" name="level['+lev+']['+curLevel[lev]+']"/></li>'+'<li style="width:80px;"><input type="text" size="6" name="mana['+lev+']['+curLevel[lev]+']"/></li>'+'<li style="width:70px;"><input type="text" size="5" name="cooldown['+lev+']['+curLevel[lev]+']"/></li>'+'<li style="width:100px;"><input type="text" size="10" name="casting['+lev+']['+curLevel[lev]+']"/></li>'+'<li style="width:100px;"><input type="text" size="10" name="area['+lev+']['+curLevel[lev]+']"/></li>'+'<li style="width:80px;"><input type="text" size="6" name="duration['+lev+']['+curLevel[lev]+']"/></li>'+'<li style="width:100px;"><input type="text" size="10" name="targets['+lev+']['+curLevel[lev]+']"/></li>'+'<li style="width:80px;"><input type="text" size="10" name="effects['+lev+']['+curLevel[lev]+']"/></li>'+'</ul><div style="clear:both;"></div>';
	ob.appendChild(objDiv);
	return false;

}
function addNote(lev)
{
	curNote[lev]++;
	var ob = document.getElementById("notes-"+lev);

	var objIn = document.createElement("input");
	objIn.className = "ltext";
	objIn.name = 's_note['+lev+']['+curNote[lev]+']';
	objIn.style.display = "block";
	ob.appendChild(objIn);
	return false;

}
function addBonus()
{
	bonusnum++;
	var ob = document.getElementById("bonus");
	var objIn = document.createElement("input");
	objIn.className = "text";
	objIn.name = "bonus["+bonusnum+"]";
	objIn.style.display = "block";
	ob.appendChild(objIn);

	return false;

}
function toggleType(val)
{
	if (val == "basic")
	{
		document.getElementById('recipe').style.display = 'none';
		document.getElementById('totprice').style.display = 'none';
	}
	else if (val == "recipe")
	{
		document.getElementById('recipe').style.display = '';
		document.getElementById('totprice').style.display = '';
	}
}



function addItem()
{
	itemnum++;
	var ob = document.getElementById("items");
	var objSelect = document.createElement("select");
	objSelect.style.marginTop = "3px";
	objSelect.name = "item["+itemnum+"]";

	var iList = document.getElementById('itemlist');
	for (optionCounter = 0; optionCounter < iList.length; optionCounter++)
	{
		var objOption = document.createElement("option");
		objOption.text = iList.options[optionCounter].text;
		objOption.value = iList.options[optionCounter].value;
		if (document.all && !window.opera) objSelect.add(objOption);
		else objSelect.add(objOption, null);
	}

	var objOr =  document.createElement("input");
	objOr.className = "stext";
	objOr.maxlength = 10;
	objOr.name = "text["+itemnum+"]";
	var objBrr= document.createElement("br");
	var objCenter= document.createElement("center");
	objCenter.style.marginTop = "10px";
	objCenter.style.marginBottom = "10px";
	objCenter.appendChild(objOr);


	var objQty = document.createElement("input");
	objQty.value = 1;
	var objBr= document.createElement("br");
	objQty.className = "xstext";
	objQty.maxlength = 2;
	objQty.name = "qty["+itemnum+"]";
	objText=document.createTextNode(" X ");
	ob.appendChild(objCenter);
	ob.appendChild(objQty);
	ob.appendChild(objText);
	ob.appendChild(objSelect);
	ob.appendChild(objBr);
	return false;
}

function addInfo()
{
	infonum++;
	var ob = document.getElementById("info");
	var objIn = document.createElement("input");
	objIn.className = "text";
	objIn.name = "info["+infonum+"]";
	objIn.style.display = "block";
	ob.appendChild(objIn);
	return false;

}

function addSkill()
{
	curSkill++;

	var htmlIN = "";
	htmlIN += '<br /><br />';
	htmlIN += '	<ul class="m">';
	htmlIN += '		<li><li><label>Type:</label><select name="s_secondary['+curSkill+']"><option value="0">Main Skill</option><option value="1">Secondary Skill</option></select></li>';
	htmlIN += '		<li><label>Skill Name:</label><input type="text" class="text" name="s_name['+curSkill+']" /> </li>';
	htmlIN += '		<li><label>Ability Type:</label><input type="text" class="text" name="s_type['+curSkill+']"/> </li>';
	htmlIN += '		<li><label>Targeting Type:</label><input type="text" class="text" name="s_targeting_type['+curSkill+']"/> </li>';
	htmlIN += '		<li><label>Ability Hotkey:</label><input type="text" class="stext" name="s_hotkey['+curSkill+']"/> </li>';
	htmlIN += '		<li><label>Icon:</label><input type="file" class="file" name="s_icon_'+curSkill+'"></li>';
	htmlIN += '		<li><label> Summary Skill:</label><textarea name="s_sumary['+curSkill+']" class="textlong"></textarea> </li>';
	htmlIN += '		<li><label> Description:</label><textarea name="s_description['+curSkill+']" class="textlong"></textarea> </li>';
	htmlIN += '		<li><label> Notes:</label>';
	htmlIN += '	<div id="notes-'+curSkill+'" style="float:left;">';
	htmlIN += '				<input type="text" class="ltext" name="s_note['+curSkill+'][0]"/>';
	htmlIN += '			</div>';
	htmlIN += '			<div style="clear:both;"></div>';
	htmlIN += '			<div align="right" style="margin-right:2px;margin-top:4px;"><a href="#" onclick="return addNote('+curSkill+');">add note line</a></div>';
	htmlIN += ' </li>';
	htmlIN += '	</ul>';


	htmlIN += '	<ul class="l">';
	htmlIN += '		<li style="width:50px;">Level</li>';
	htmlIN += '		<li style="width:80px;">Mana Cost</li>';
	htmlIN += '		<li style="width:70px;">Cooldown</li>';
	htmlIN += '		<li style="width:100px;">Casting range</li>';
	htmlIN += '		<li style="width:100px;">Area of Effect</li>';
	htmlIN += '		<li style="width:80px;">Duration</li>';
	htmlIN += '		<li style="width:100px;">Allowed Targets</li>';
	htmlIN += '		<li style="width:80px;">Effects</li>';
	htmlIN += '	</ul>';
	htmlIN += '	<div id="levels-'+curSkill+'">';
	htmlIN += '		<ul class="l">';
	htmlIN += '			<li style="width:50px;"><input type="text" size="2" name="level['+curSkill+'][0]"/></li>';
	htmlIN += '			<li style="width:80px;"><input type="text" size="6" name="mana['+curSkill+'][0]"/></li>';
	htmlIN += '			<li style="width:70px;"><input type="text" size="5" name="cooldown['+curSkill+'][0]"/></li>';
	htmlIN += '			<li style="width:100px;"><input type="text" size="10" name="casting['+curSkill+'][0]"/></li>';
	htmlIN += '			<li style="width:100px;"><input type="text" size="10" name="area['+curSkill+'][0]"/></li>';
	htmlIN += '			<li style="width:80px;"><input type="text" size="6" name="duration['+curSkill+'][0]"/></li>';
	htmlIN += '			<li style="width:100px;"><input type="text" size="10" name="targets['+curSkill+'][0]"/></li>';
	htmlIN += '			<li style="width:80px;"><input type="text" size="10" name="effects['+curSkill+'][0]"/></li>';
	htmlIN += '		</ul><div style="clear:both;"></div>';
	htmlIN += '		';
	htmlIN += '	</div>';
	htmlIN += '	<div style="clear:both;"></div>';
	htmlIN += '	<div align="right" style="margin-right:2px;margin-top:4px;"><a href="#" onclick="return addLevel('+curSkill+');">add level</a></div>';

	var objDiv = document.createElement("div");
	objDiv.innerHTML = htmlIN;
	document.getElementById('skills').appendChild(objDiv);
	curLevel[curSkill] = 0;
	curNote[curSkill] = 0;
	return false;
}



function form_set_select(sel_name, form_name, sel_index){
	if ((form_name != "") && (typeof eval("document." + form_name + "." + sel_name) == "object")) {
		sel_length = eval("document." + form_name + "." + sel_name + ".length");
		for (optionCounter = 0; optionCounter < sel_length; optionCounter++) {
			if (eval("document." + form_name + "." + sel_name + ".options[optionCounter].value == '" + sel_index + "'")) {
				eval("document." + form_name + "." + sel_name + ".selectedIndex = optionCounter");
			}
		}
	}
}

function showHint(obj, text)
{
	obj.onblur = function() { document.getElementById('hint').style.display = '';document.getElementById('hint-pointer').style.display = '';};
	document.getElementById('hint').style.display = '';
	var w = obj.offsetWidth;
	var curleft = 0;
	var curtop = 0;
	if (obj.offsetParent) {
		do {
			curleft += obj.offsetLeft;
			curtop += obj.offsetTop;
		} while (obj = obj.offsetParent);
	}

	document.getElementById('hint').innerHTML = text;

	document.getElementById('hint').style.top = curtop+"px";
	document.getElementById('hint').style.left = (curleft+w)+20+"px";

	document.getElementById('hint').style.display = 'inline';


	document.getElementById('hint-pointer').style.top = curtop+"px";
	document.getElementById('hint-pointer').style.left = (curleft+w)+11+"px";

	document.getElementById('hint-pointer').style.display = 'inline';

	setOpacity('hint', 0);
	setOpacity('hint-pointer', 0);
}

function setOpacity(id, value) {

	testObj = document.getElementById(id);
	testObj.style.opacity = value/10;
	testObj.style.filter = 'alpha(opacity=' + value*10 + ')';

	if (value < 10)
	{

		value = (value+1);
		window.setTimeout("setOpacity('"+id+"', "+value+")", 30);
	}
	else
	{
		testObj.style.opacity = '';
		testObj.style.filter = '';
	}
}

function delOpacity(id, value) {

	testObj = document.getElementById(id);
	testObj.style.opacity = value/10;
	testObj.style.filter = 'alpha(opacity=' + value*10 + ')';

	if (value > 0)
	{

		value = (value-1);
		window.setTimeout("delOpacity('"+id+"', "+value+")", 90);
	}
	else
	{
		testObj.style.display = 'none';
	}
}



function createCookie(name,value,days) {
	if (days) {
		var date = new Date();
		date.setTime(date.getTime()+(days*24*60*60*1000));
		var expires = "; expires="+date.toGMTString();
	}
	else var expires = "";
	document.cookie = name+"="+value+expires+"; path=/";
}

function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}

function correctPNG() // correctly handle PNG transparency in Win IE 5.5 & 6.
{
	var arVersion = navigator.appVersion.split("MSIE")
	var version = parseFloat(arVersion[1])
	if ((version >= 5.5) && (document.body.filters))
	{
		for(var i=0; i<document.images.length; i++)
		{
			var img = document.images[i]
			var imgName = img.src.toUpperCase()
			if (imgName.substring(imgName.length-3, imgName.length) == "PNG")
			{
				var imgID = (img.id) ? "id='" + img.id + "' " : ""
				var imgClass = (img.className) ? "class='" + img.className + "' " : ""
				var imgTitle = (img.title) ? "title='" + img.title + "' " : "title='" + img.alt + "' "
				var imgStyle = "display:inline-block;" + img.style.cssText
				imgStyle = "float:left;" + imgStyle
				if (img.parentElement.href) imgStyle = "cursor:hand;" + imgStyle
				var strNewHTML = "<span " + imgID + imgClass + imgTitle
				+ " style=\"" + "width:" + img.width + "px; height:" + img.height + "px;" + imgStyle + ";"
				+ "filter:progid:DXImageTransform.Microsoft.AlphaImageLoader"
				+ "(src=\'" + img.src + "\', sizingMethod='scale');\"></span>"
				img.outerHTML = strNewHTML
				i = i-1
			}
		}
	}
}

var locked = 0;
var lastimg = 0;
function showItem(item, lock, obj)
{
	if (lock == 2) { obj = document.getElementById('it'+item); lock = 1}
	if (item == 0) return;
	if (lock == 1)
	{
		if (obj) obj.parentNode.className = 'ons';
		if (locked == item)
		{
			// obj.onmouseout = function() { document.getElementById('iright').style.display = 'none'; };
			locked = 0;
			obj.parentNode.className = '';
			return false;
		}
		else if (locked != 0) lastimg.parentNode.className = '';

		locked = item;
		lastimg = obj;
	}
	else
	if (locked != 0) return false;
	else
	{
		if (lastimg) lastimg.parentNode.className = '';
		if (obj != "this") obj.parentNode.className = 'on';
		if (obj != "this") lastimg = obj;
	}


	populateItem(IT[item]);
	//var URL = "/remote/items.php";
	//remote_data_request(URL, "item="+item, "populateItem(http_remote_result);");
	return false;
}
var OLDPAR = '';
function showHero(hero, obj)
{

	if (hero < 1) return;
	if (OLDPAR != '') OLDPAR.className = "";

	if (obj)
	{obj.parentNode.className = "on";
	OLDPAR = obj.parentNode;}

	populateHero(HD[hero]);

	return false;
}

function initnav(type)
{
	document.getElementById('filta').className = '';
	document.getElementById('filtg').className = '';
	document.getElementById('filtc').className = '';
	PAGE = 0;
	ONPAGE = 10;
	TOTAL = 0;

	if (type == 0)
	{
		WHO = NEWS;
		document.getElementById('filta').className = 'on';

	}
	else
	{
	(type == 1)?document.getElementById('filtg').className = 'on':document.getElementById('filtc').className = 'on';
	WHO = new Array();
	NEWS.each(function(item)
	{
		if (item)
		{
			xml = item;
			xmlString = loadXMLString(xml);
			n = xmlString.getElementsByTagName('rang')[0].childNodes[0].nodeValue;
			if (xmlString.getElementsByTagName('t')[0].childNodes[0].nodeValue == type) WHO[n] = NEWS[n];
		}
	});
	}
	jsnav('next');
}
var ONFANART = 0;
var ONVIDEO = 0;
function updateModerator(key)
{

	dom_toggle_element('addcom', 1);
	dom_toggle_element('comnav', 1);
	if (document.getElementById('pagetext')) document.getElementById('pagetext').value = 'Post your comment here';
	if (document.getElementById('key')) document.getElementById('key').value = key;
	document.getElementById('imagedetails').style.display = 'inline';


	if (ONFANART) xml = FANART[key];
	else if (ONVIDEO) xml = VIDEOS[key];
	else xml = COMICS[key];
	xmlString = xml;




	inner('it', xmlString.title);
	if (xmlString.desc)
	if (xmlString.desc.length > 2)
	{


		// $('descriptionDiv').update('<b>Description: </b>'+xmlString.desc);	
	if ($('descText')) $('descText').update(xmlString.desc);	
		// $('descriptionDiv').setStyle({display:''});
	}
	
	if (ONFANART) inner('io', xmlString.orig);
	inner('ia', xmlString.author);
	inner('dpd', xmlString.date);
	inner('lcd', xmlString.lc);
	inner('tv', xmlString.votes);
	inner('cr', xmlString.rate);
	if (ONVIDEO) inner('origauthor', xmlString.ora);

	if (ONFANART) inner('permlink', "(<a href='/fanart/"+key+"'>Permanent link</a>)");
	else if (!ONVIDEO) inner('permlink', "(<a href='/comics/"+key+"'>Permanent link</a>)");

	if (document.getElementById('rsd')) inner('rsd', xmlString.rez);
	if (document.getElementById('fld')) inner('fld', xmlString.size);

	getComments(xmlString.forum, 1);
	if (ONFANART) p = "fanart";
	else if (ONVIDEO) p = "videos";
	else p = "comics";
	if (document.getElementById('editor'))
	{
		document.getElementById('editor').style.display = '';
		if (document.getElementById('delitem')) document.getElementById('delitem').href = "/"+p+"/"+key+"/delete";
		if (document.getElementById('edititem')) document.getElementById('edititem').href = "/add/"+p+"/"+key;
		if (document.getElementById('spotitem')) document.getElementById('spotitem').href =  "/"+p+"/"+key+"/spotlight";

		var curleft = curtop = 0;
		var obj = document.getElementById('editor');
		if (obj.offsetParent) {
			do {
				curleft += obj.offsetLeft;
				curtop += obj.offsetTop;
			} while (obj = obj.offsetParent);
		}
		document.getElementById('editor').style.position='absolute';
		document.getElementById('editor').style.left = curleft-120+'px';
		document.getElementById('editor').style.top = (curtop+50)+'px';
		document.getElementById('editor').style.zIndex = '220';
	}
}

var PAGE;
var ONPAGE;
var TOTAl;
var WHO;
var P = 0;

function inner(id, text)
{
	var len = document.getElementById(id).childNodes.length;

	for(var i = 0; i < len; i++)
	{
		document.getElementById(id).removeChild(document.getElementById(id).childNodes[i]);
	}
	var t = document.createElement('span');
	t.innerHTML = text;
	document.getElementById(id).appendChild(t);
}


function restoreNews()
{

	populateNews(ORLEFT);
	populateNews(ORRIGHT);
}
function jsnav(where)
{
	if (TOTAL == 0)
	WHO.each(function(item)
	{
		if (item) TOTAL++;
	});

	s=0;
	tot=0;
	UL = "<ul>";
	if (where == 'prev') PAGE = PAGE-2;
	start = PAGE*ONPAGE;
	WHO.each(function(item)
	{

		if (item)
		{
			if (s++ < start) a = 1;
			else
			{

				tot++;
				xml = item;
				xmlString = loadXMLString(xml);

				k = xmlString.getElementsByTagName('key')[0].childNodes[0].nodeValue;
				t = xmlString.getElementsByTagName('title')[0].childNodes[0].nodeValue;
				c = xmlString.getElementsByTagName('col')[0].childNodes[0].nodeValue;
				d = xmlString.getElementsByTagName('navdate')[0].childNodes[0].nodeValue;
				s = xmlString.getElementsByTagName('seo')[0].childNodes[0].nodeValue;
				if (xmlString.getElementsByTagName('sp')[0].childNodes[0].nodeValue == 1)
				spclass = 'or';
				else spclass = '';
				if (tot%2 == 0) cls = "on"; else cls="";
				UL += '	<li class="'+cls+'"  onmouseover="populateNews('+NEWS.indexOf(item)+');" onmouseout="restoreNews();"><a href="/news/'+s+'" ><span class="gr">['+d+']</span> <span class="'+c+'" onmouseover="this.className=\'or\'" onmouseout="this.className=\''+c+'\'"><span id="newslink'+NEWS.indexOf(item)+'" class='+spclass+'>'+t+'</span></span></a></li>';
				if (tot == ONPAGE) throw $break;
			}
		}
	});

	PAGE++;
	UL += "</ul>";
	document.getElementById('jsnav').innerHTML = UL;
	if (PAGE*ONPAGE >= TOTAL) document.getElementById('navnext').style.display = 'none';
	else document.getElementById('navnext').style.display = '';

	if (PAGE-1 == 0) document.getElementById('navprev').style.display = 'none';
	else document.getElementById('navprev').style.display = '';
	restoreNews();
}

var ORLEFT;
var ORRIGHT;
var lastleft = '';
var lastright = '';
function populateNews(key)
{
	if (PASS == 1) return;

	xml = NEWS[key];
	if (xml == null) return;
	xmlString = loadXMLString(xml);

	w = xmlString.getElementsByTagName('pos')[0].childNodes[0].nodeValue;

	inner("n"+w+"t", "<a href='/news/"+xmlString.getElementsByTagName('seo')[0].childNodes[0].nodeValue+"'>"+xmlString.getElementsByTagName('title')[0].childNodes[0].nodeValue)+"</a>";
	inner("n"+w+"u", "<a href='/forums/member.php?u="+xmlString.getElementsByTagName('userid')[0].childNodes[0].nodeValue+"'>"+xmlString.getElementsByTagName('author')[0].childNodes[0].nodeValue+"</a>");
	inner("n"+w+"p", decodeURIComponent(xmlString.getElementsByTagName('prev')[0].childNodes[0].nodeValue));
	inner("n"+w+"p", decodeURIComponent(xmlString.getElementsByTagName('prev')[0].childNodes[0].nodeValue));
	inner("n"+w+"d", decodeURIComponent(xmlString.getElementsByTagName('date')[0].childNodes[0].nodeValue));
	if (parseInt(xmlString.getElementsByTagName('read')[0].childNodes[0].nodeValue) == 1)
	{
		document.getElementById("n"+w+"r").href = "/news/"+xmlString.getElementsByTagName('seo')[0].childNodes[0].nodeValue;
		document.getElementById("n"+w+"r").style.display = '';
		inner("n"+w+"r", "Read more");
	} else
	{
		document.getElementById("n"+w+"r").href = "/news/"+xmlString.getElementsByTagName('seo')[0].childNodes[0].nodeValue;
		document.getElementById("n"+w+"r").style.display = '';
		inner("n"+w+"r", "Comment here");
	}

}


function populateHero(xml)
{

	if (xml == null) return;
	xmlString = loadXMLString(xml);
	document.getElementById('iName').src = "http://media.playdota.com/hero/"+xmlString.getElementsByTagName('key')[0].childNodes[0].nodeValue+"/"+xmlString.getElementsByTagName('icon')[0].childNodes[0].nodeValue;
	document.getElementById('dC').innerHTML = xmlString.getElementsByTagName('name')[0].childNodes[0].nodeValue;
	document.getElementById('dT').innerHTML =  xmlString.getElementsByTagName('class')[0].childNodes[0].nodeValue;
	document.getElementById('strength').innerHTML = xmlString.getElementsByTagName('strength')[0].childNodes[0].nodeValue;
	document.getElementById('agility').innerHTML = xmlString.getElementsByTagName('ability')[0].childNodes[0].nodeValue;
	document.getElementById('intelligence').innerHTML = xmlString.getElementsByTagName('intelligence')[0].childNodes[0].nodeValue;
	document.getElementById('as').innerHTML = decodeURIComponent(xmlString.getElementsByTagName('stats')[0].childNodes[0].nodeValue.replace("+", " "));
	document.getElementById('sk').innerHTML = decodeURIComponent(xmlString.getElementsByTagName('skills')[0].childNodes[0].nodeValue.replace("+", " "));

	document.getElementById('sc').src = "/img/site/strength.jpg";
	document.getElementById('ac').src = "/img/site/agility.jpg";
	document.getElementById('ic').src = "/img/site/intelligence.jpg";

	hc = xmlString.getElementsByTagName('hclass')[0].childNodes[0].nodeValue;
	if (hc == 1) document.getElementById('sc').src = "/img/site/strength-c.jpg";
	if (hc == 2) document.getElementById('ac').src = "/img/site/agility-c.jpg";
	if (hc == 3) document.getElementById('ic').src = "/img/site/intelligence-c.jpg";
	document.getElementById('iright').style.display = '';
}
function populateItem(xml)
{
	if (xml == null) return;

	xmlString = loadXMLString(xml);

	var key = xmlString.getElementsByTagName('key')[0].childNodes[0].nodeValue;
	$('iName').src = "http://media.playdota.com/items/"+key+"/"+xmlString.getElementsByTagName('text')[0].childNodes[0].nodeValue;
	$('iName').style.display = "block";

	$('iIcon').src = "http://media.playdota.com/items/"+key+"/"+xmlString.getElementsByTagName('icon')[0].childNodes[0].nodeValue;
	$('iIcon').style.display = "inline";

	document.getElementById('iPrice').innerHTML = xmlString.getElementsByTagName('price')[0].childNodes[0].nodeValue;
	$('iShop').innerHTML = xmlString.getElementsByTagName('shop')[0].childNodes[0].nodeValue;

	$('palink').href = '/items/'+xmlString.getElementsByTagName('seo')[0].childNodes[0].nodeValue;

	document.getElementById('iDesc').innerHTML = xmlString.getElementsByTagName('desc')[0].childNodes[0].nodeValue;

	var iinfo = "";
	for (x=0;x<xmlString.getElementsByTagName('info')[0].childNodes.length;x++)
	{
		try {
			if (xmlString.getElementsByTagName('info')[0].childNodes[x].nodeValue != null)
			iinfo += xmlString.getElementsByTagName('info')[0].childNodes[x].nodeValue+"<br />";

		} catch(e) {}
	}

	var ibonus = "";
	for (x=0;x<xmlString.getElementsByTagName('bonus')[0].childNodes.length;x++)
	{
		try {
			if (xmlString.getElementsByTagName('bonus')[0].childNodes[x].nodeValue != null)
			ibonus += xmlString.getElementsByTagName('bonus')[0].childNodes[x].nodeValue+"<br />";

		} catch(e) {}
	}


	document.getElementById('iInfo').innerHTML = iinfo;
	document.getElementById('iBonus').innerHTML = ibonus;

	RItem = xmlString.getElementsByTagName('r');
	document.getElementById('related').innerHTML = "";
	for (x=0;x<RItem.length;x++)
	{
		htmlIN = "";
		if (xmlString.getElementsByTagName('type')[0].childNodes[0].nodeValue == "recipe" && xmlString.getElementsByTagName('rtext')[x].childNodes[0].nodeValue && xmlString.getElementsByTagName('rtext')[x].childNodes[0].nodeValue != 'none')
		htmlIN += "<center>"+xmlString.getElementsByTagName('rtext')[x].childNodes[0].nodeValue+"</center>";

		htmlIN += '<a href="#" onclick="return showItem('+xmlString.getElementsByTagName('rkey')[x].childNodes[0].nodeValue+', 2, this);"><img src="http://media.playdota.com/items/'+xmlString.getElementsByTagName('rkey')[x].childNodes[0].nodeValue+'/'+xmlString.getElementsByTagName('ricon')[x].childNodes[0].nodeValue+'" align="middle"/></a>';

		htmlIN +=  xmlString.getElementsByTagName('rname')[x].childNodes[0].nodeValue;
		htmlIN += ' <span>('+xmlString.getElementsByTagName('rprice')[x].childNodes[0].nodeValue+')</span> <br />';
		document.getElementById('related').innerHTML += htmlIN;
	}
	if (document.getElementById('related').innerHTML == "") document.getElementById('related').innerHTML = "None";
	if (xmlString.getElementsByTagName('type')[0].childNodes[0].nodeValue == "recipe")
	document.getElementById('related').className = "recipe";
	else document.getElementById('related').className = "usedin";

	// RECIPE USED IN
	RIUin = xmlString.getElementsByTagName('rr');
	$('relatedin').style.display = 'none';
	$('relatedin').innerHTML = '';
	for (x=0;x<RIUin.length;x++)
	{
		htmlIN = "";
		if (xmlString.getElementsByTagName('type')[0].childNodes[0].nodeValue == "recipe" && xmlString.getElementsByTagName('rrtext')[x].childNodes[0].nodeValue && xmlString.getElementsByTagName('rrtext')[x].childNodes[0].nodeValue != 'none')
		htmlIN += "<center>"+xmlString.getElementsByTagName('rrtext')[x].childNodes[0].nodeValue+"</center>";

		htmlIN += '<a href="#" onclick="return showItem('+xmlString.getElementsByTagName('rrkey')[x].childNodes[0].nodeValue+', 2, this);"><img src="http://media.playdota.com/items/'+xmlString.getElementsByTagName('rrkey')[x].childNodes[0].nodeValue+'/'+xmlString.getElementsByTagName('rricon')[x].childNodes[0].nodeValue+'" align="middle"/></a>';

		htmlIN +=  xmlString.getElementsByTagName('rrname')[x].childNodes[0].nodeValue;
		htmlIN += ' <span>('+xmlString.getElementsByTagName('rrprice')[x].childNodes[0].nodeValue+')</span> <br />';
		document.getElementById('relatedin').innerHTML += htmlIN;
		document.getElementById('relatedin').style.display = '';
	}


	document.getElementById('iright').style.display = "";

	if (document.getElementById('delitem')) document.getElementById('delitem').href = "/items/"+key+"/delete";
	if (document.getElementById('edititem')) document.getElementById('edititem').href = "/add/item/"+key;
}

function loadXMLString(txt)
{
	try //Internet Explorer
	{
		xmlDoc=new ActiveXObject("Microsoft.XMLDOM");
		xmlDoc.async="false";
		xmlDoc.loadXML(txt);
		return xmlDoc;
	}
	catch(e)
	{
		try //Firefox, Mozilla, Opera, etc.
		{
			parser=new DOMParser();
			xmlDoc=parser.parseFromString(txt,"text/xml");
			return xmlDoc;
		}
		catch(e) {alert(e.message)}
	}
	return null;
}

function populateComments(xml)
{
	cObj = document.getElementById('comlist');
	cObj.innerHTML = "";

	if (xml == 'nan')
	{
		cObj.innerHTML = "<br /><center><b><span class='or'>No comments yet</span></b></center>";
		dom_toggle_element('addcom', 1);
		return;
	}
	xmlStr = loadXMLString(xml);
	max = xmlStr.getElementsByTagName('cc').length;
	for (x=0;x<max;x++)
	{
		cObj.innerHTML += '<span class="blw">'+xmlStr.getElementsByTagName('cu')[x].childNodes[0].nodeValue+': </span>';
		cObj.innerHTML += '<span class="gr">'+xmlStr.getElementsByTagName('ct')[x].childNodes[0].nodeValue+'</span><span style="display:block;"> </span><br /> ';
	}
	// NAVIGATION
	var nav = xmlStr.getElementsByTagName('cn')[x-1].childNodes[0].nodeValue.split("|");
	commentsNav(nav[1], nav[0], xmlStr.getElementsByTagName('ck')[x-1].childNodes[0].nodeValue);


	return;

}
function getComments(key, page)
{
	if(document.getElementById('forum')) document.getElementById('forum').value = key;
	cObj = document.getElementById('comlist');
	cObj.innerHTML = "<center><img src='/img/site/loadingcomments.gif' align='middle' /> <span class='blw'><b>Please wait ...</b></span></center>";

	url = "/remote/comments.php";
	if (key) remote_data_request(url, "cmd=get&page="+page+"&key="+key, "populateComments(http_remote_result);");
}

// REMOTE REQUEST FUNCTIONS
var http_request = false;
var http_remote_result = "";

function remote_data_request(url, parameters, callback_function) {

	http_request = false;
	if (window.XMLHttpRequest) { // Mozilla, Safari,...
		http_request = new XMLHttpRequest();
		if (http_request.overrideMimeType) {
			http_request.overrideMimeType("text/html");
		}
	}
	else if (window.ActiveXObject) { // IE
		try {
			http_request = new ActiveXObject("Msxml2.XMLHTTP");
		}
		catch (e) {
			try {
				http_request = new ActiveXObject("Microsoft.XMLHTTP");
			}
			catch (e) {}
		}
	}
	if (!http_request) {
		alert("Cannot create XMLHTTP instance");
		return false;
	}

	http_request.onreadystatechange = function(){
		if (http_request.readyState == 4) {
			if (http_request.status == 200) {
				http_remote_result = http_request.responseText;
				if (callback_function)
				eval(callback_function);
				else eval(http_remote_result);
			}
			else {
				alert("There was a problem with the request.");
			}
		}
	};

	http_request.open('POST', url, true);
	http_request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	http_request.setRequestHeader("Content-length", parameters.length);
	http_request.setRequestHeader("Connection", "close");
	http_request.send(parameters);

}

function dom_get_element(id){
	var obj;

	if (document.all) {
		eval('obj = document.all("' + id + '")');
	}
	else if (document.layers) {
		eval('obj = document.layers["' + id + '"]');
	}
	else if (document.getElementById) {
		eval('obj = document.getElementById("' + id + '")');
	}

	return obj;
}


function getObjByName(name,doc) {
	var o = 0;
	if(!doc) {
		doc = document;
	}
	if(doc[name]) {
		o=doc[name];
	}
	if(document.all && doc.all[name]) {
		o=doc.all[name];
	}
	if(o) {
		if(!o.getElementsByTagName) {
			o.getElementsByTagName = getElementsArray;
		}
		return o;
	}
	if(document.layers) {
		for(var i=0; i < doc.layers.length; i++){
			var lyrdoc = doc.layers[i].document;
			if(lyrdoc[name]) {
				return lyrdoc[name];
			}
			if(lyrdoc.layers.length > 0) {
				var o = getObjByName(name,lyrdoc);
				if(o) {
					return o;
				}
			}
		}
	}
	return 0;
}

function textCounter(field, cntfield, maxlimit) {
	var obj_field = document.getElementById(field);

	if (obj_field.value.length > 20) obj_field.style.height="100px";

	//if (obj_field.value.length > maxlimit){
	//	obj_field.value = obj_field.value.substring(0, maxlimit);
	//}

}

function addComment(obj)
{
	text = obj.pagetext.value;
	if (text.length < 3) alert("C'mon, you can enter at least 3 characters right ?")
	if (text == "Post your comment here") alert("Enter a comment");
	//else if (text.length > 100) alert("Hey, no more than 100 characters");
	else
	{
		dom_toggle_element('addcom', 0);
		url = "/remote/comments.php";
		remote_data_request(url, "cmd=add&forum="+obj.forum.value+"&text="+encodeURIComponent(text), "addCommentSucces("+obj.forum.value+");");
	}
	return false;
}

function addCommentSucces(key)
{
	dom_toggle_element('addcom', 0);
	dom_toggle_element('comsuc', 1);
	document.getElementById('pagetext').value = '';
	getComments(key, 1);
}
function dom_toggle_element(el, visible){

	if (document.getElementById(el))
	{
		if (visible == 1) document.getElementById(el).style.display = '';
		else if (visible == 0) document.getElementById(el).style.display = 'none';
		else
		if (document.getElementById(el).style.display != 'none')
		document.getElementById(el).style.display = 'none'
		else document.getElementById(el).style.display = ''
	}
	return false;
}

function dom_toggle(el, visible){

	if (document.getElementById(el))
	{
		if (visible == 1) document.getElementById(el).style.display = '';
		else if (visible == 0) document.getElementById(el).style.display = 'block';
		else
		if (document.getElementById(el).style.display != 'block')
		document.getElementById(el).style.display = 'block'
		else document.getElementById(el).style.display = ''
	}
	return false;
}

function herotoggle(type, obj)
{

	for (i=0;i<document.getElementById('menuhero').getElementsByTagName('a').length;i++)
	{
		document.getElementById('menuhero').getElementsByTagName('a')[i].className = '';
	}

	dom_toggle_element('info', 0);
	dom_toggle_element('comments', 0);
	dom_toggle_element('guides', 0);
	dom_toggle_element('art', 0);
	dom_toggle_element('replays', 0);
	dom_toggle_element('video', 0);
	dom_toggle_element('builder', 0);
	dom_toggle_element('sounds', 0);
	dom_toggle_element(type, 1);
	obj.className = 'on';

	return false;
}

function dom_get_element(id){
	var obj;

	if (document.all) {
		eval('obj = document.all("' + id + '")');
	}
	else if (document.layers) {
		eval('obj = document.layers["' + id + '"]');
	}
	else if (document.getElementById) {
		eval('obj = document.getElementById("' + id + '")');
	}

	return obj;
}

function commentsNav(T, P, K)
{
	nextp = (parseInt(P)+1);
	NAV = '<ul class="navigation">';
	if (P > 1) NAV += 		'<li><a href="#" onclick="getComments('+K+', 1);return false;"><img src="/img/site/nav/first.jpg" border="0" alt="first" /></a></li>';
	if (P > 1) NAV +=		'<li><a href="#" onclick="getComments('+K+', '+(P-1)+');return false;"><img src="/img/site/nav/prev.jpg" border="0" alt="prev" /></a></li>';
	NAV +=		'<li>Page '+P+' / '+T+'</li>';
	if (P < T) NAV +=		'<li><a href="#" onclick="getComments('+K+', '+nextp+');return false;"><img src="/img/site/nav/next.jpg" border="0" alt="next" /></a></li>';
	if (P < T) NAV +=		'<li><a href="#" onclick="getComments('+K+', '+T+');return false;"><img src="/img/site/nav/last.jpg" border="0" alt="last"/></a></li>';
	NAV +=	'</ul>';
	document.getElementById('comnav').innerHTML = NAV;
	dom_toggle_element('comnav', 1);
}

function rateObj(obj)
{
	val = obj.rate.value;
	type = obj.type.value;
	key = obj.key.value;
	if (val <= 10 && val >= 1)
	{
		remote_data_request("/remote/comments.php", "cmd=rate&key="+key+"&rate="+val+"&type="+type, "eval(http_remote_result);");
	} else alert("Please select a rate");
	document.getElementById('rate').selectedIndex = 0;
	return false;
}


function checkthisform(obj)
{

	inputs = document.getElementsByTagName('input');
	for (i=0;i < inputs.length;i++)
	{
		alert(inputs[i].rel);
	}
	return false;
}
