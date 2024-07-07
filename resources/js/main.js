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
playb = null;
function play(){
  gi("aud").play();
  gi("vid").play();
  gi("vid").controls = true;
  playb = setInterval(function(){
	  if (gi("vid").readyState < 3){
		  gi("aud").pause();
	  } else {
		  if (gi("aud").paused){
		    gi("aud").play();
		  }
	  }
	  if (gi("aud").readyState < 3){
		  gi("vid").pause();
	  } else {
		  if (gi("vid").paused){
		    gi("vid").play();
		  }
	  }
	  if (Math.abs(gi("vid").currentTime - gi("aud").currentTime) > 0.3){
		  gi("aud").currentTime = gi("vid").currentTime;
	  }
  }, 10);
}
