function getBotResponse() {
    var rawText = $("#textInput").val();
    var userHtml = '<p class="userText"><span>' + rawText + "</span></p>";
    $("#textInput").val("");
    $("#chatbox").append(userHtml);
    document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
    $.get("/get", { msg: rawText }).done(function(data) {
        var botHtml = '<p class="botText"><span>' + data + "</span></p>";
        $("#chatbox").append(botHtml);
        document.getElementById("userInput").scrollIntoView({ block: "start", behavior: "smooth" });
    });
}

$(document).keypress(function(e) {
    console.log(e.which)
    if (e.which == 13) {
        getBotResponse();
        console.log('test')
    }
});

// $(document).keydown(function(e){
//     if (e.keyCode == 13) {
//        alert( "right arrow pressed" );
//        return false;
//     }
// });