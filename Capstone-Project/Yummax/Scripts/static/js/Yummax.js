function button_toggle() {
    var x = document.getElementById("explore");
    var y = document.getElementById("form");
    
    x.style.display = "none";
    y.style.display = "block";
}

function submit_toggle() {
    var x = document.getElementById("explore");
    var y = document.getElementById("form");
    
    y.style.display = "none";
    x.style.display = "block";
}

function but_toggle() {
    var a = document.getElementById("sift");
    var b = document.getElementById("form_dining");
    
    a.style.display = "none";
    b.style.display = "block";
}

function sub_toggle() {
    var a = document.getElementById("sift");
    var b = document.getElementById("form_dining");
    
    b.style.display = "none";
    a.style.display = "block";
}

function initMap() {
    var dsi = {lat: 1.3077, lng: 103.8318};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 17,
      center: dsi
    });
    var marker = new google.maps.Marker({
      position: dsi,
      map: map
    });
}