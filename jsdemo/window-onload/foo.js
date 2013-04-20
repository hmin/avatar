function registerNewFunc(entryFunc, newFunc) {
	return function() {
	  if (entryFunc) entryFunc();
	  if (newFunc) newFunc();
	}
}

function foo() {
	document.getElementById("content").innerHTML += "call foo in foo.js<br>"
}

window.onload = registerNewFunc(window.onload, foo);