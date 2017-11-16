function show_login() {
    var x = document.getElementById("login_form");   
    x.style.display = "block";
}

function show_msg () {
    var msg = document.getElementById('msg');
    var message;
    
    message = "Shamelessly scraping tweets and foodie blogs\
\.... please wait";
    
    msg.innerHTML = message;
}

