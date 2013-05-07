function $(id) {
  return document.getElementById(id);
}

function exitFullscreen() {
  //if (document.webkitIsFullscreen) {
    document.webkitExitFullscreen();
    $("toggleElem").onclick = enterFullscreen;
    $("toggleElem").value = "Fullscreen <div>";
  //}
}

function enterFullscreen() {
  //if (!document.webkitIsFullscreen) {
    $("content").webkitRequestFullscreen();
    $("toggleElem").onclick = exitFullscreen;
    $("toggleElem").value = "Exit Fullscreen <div>";
  //}
}

function fullscreenWindow() {
  if (!chrome.app.window.current().isFullscreen()) {
    chrome.app.window.current().fullscreen();
    $("toggleWindow").onclick = restoreWindow;
    $("toggleWindow").value = "Restore Window";
  }
}

function restoreWindow() {
  if (chrome.app.window.current().isFullscreen()) {
    chrome.app.window.current().restore();
    $("toggleWindow").onclick = fullscreenWindow;
    $("toggleWindow").value = "Fullscreen Window";
  }
}

function init() {
  $("toggleElem").onclick = enterFullscreen;
  $("toggleElem").value = "Fullscreen <div>";

  fullscreenWindow();
}

window.onload = init;
