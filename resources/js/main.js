function as(u) {
var e = document.createElement('script');
e.src = u;
document.body.appendChild(e);
};
var d = document;
var gi = function(m){
	return document.getElementById(m);
};
var gc = function(m){
	return document.getElementsByClassName(m);
};
function loaded(){
	var load = gc("load")[0];
	var i = 1;
	var t = setInterval(function(){
		load.style.opacity = i;
		i -= 0.01;
		if(i <= 0){
			load.style.display = "none";
			clearInterval(t);
		}
	}, 15);
}
