
function choosebanksgd () {
    var sgdamt = document.getElementById('sgd-amt-id');
    var amtsel = sgdamt.options;
    var sgddur = document.getElementById('sgd-dur-id');
    var dursel = sgddur.options;
    var message;

    var sgdoutput = document.getElementById('sgdoutput-id');

    if (amtsel[1].value == "<5000" && dursel[0].value == "1 year") {
        message = 'JuneBank has highest interest of 2.88%';
    }    else {
        message = 'United Local Bank has highest interest of 3.88%';
    }
    sgdoutput.innerHTML = message;
}

function choosebankcur () {
    var cur = document.getElementById('cur-id');
    var cursel = cur.options;
    var curamt = document.getElementById('cur-amt-id');
    var amtsel = curamt.options;
    var curdur = document.getElementById('cur-dur-id');
    var dursel = curdur.options;
    var message;

    var curoutput = document.getElementById('curoutput-id');

    if (cursel[0].value == "usd" && amtsel[1].value == "<5000" && dursel[0].value == "1 year") {
        message = 'Captain America Bank has highest interest of 2.88%';
    }    else {
        message = 'Galaxy Bank has highest interest of 6.88%';
    }
    curoutput.innerHTML = message;
}
