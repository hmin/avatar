function bar() {
	document.getElementById("content").innerHTML += "call bar in bar.js<br>"
}

window.onload = registerNewFunc(window.onload, bar);