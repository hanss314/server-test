function sendRequest() {
    var xhttp = new XMLHttpRequest();
    var text = document.getElementById("text").value;
    xhttp.onload = function() {
        if (this.readyState == 4) {
            document.getElementById("demo").innerHTML = this.responseText;
        }
    };
    xhttp.open("POST", window.location.pathname, true);
    xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    xhttp.send(text);
}
