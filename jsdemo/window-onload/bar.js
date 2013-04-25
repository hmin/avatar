function bar() {
	document.getElementById("content").innerHTML += "call bar in bar.js<br>"
}

registerNewFuncIntoArray(bar);
//window.onload = registerNewFunc(window.onload, bar);
