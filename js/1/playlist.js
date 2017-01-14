window.onload = init;

function init() {
	var button = document.getElementById('addButton');
	button.onclick = buttonClickHandler;
}

function buttonClickHandler() {
	var textInput = document.getElementById('songTextInput');
	var songName = textInput.value;
	if (songName == ""){
		alert("please enter a song");
	}
	else{
		var li = document.createElement("li");
		li.innerHTML = songName;
		var ul = document.getElementById("playlist");
		ul.appendChild(li);
	}
	
}

