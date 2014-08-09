$.ajax({
    "url":"http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce&callback=kimonoCallback",
    "crossDomain": true,
    "dataType": "jsonp"
});

function kimonoCallback(e){
    var last = e.lastsuccess;
    e = e["results"]
    var ans = e["Answer Data"];
    e = e["Question Data"][0];
    $("#data").prepend("<div id='first'><span id='date'>" + e.Date + " </span><span id='last'>Last Updated: " + last + "</span><br><br><span id='intro'>Today's question is categorized as <strong><span id='type'>" + e["Type of Question"] + "</span></strong>.</span><br><br><strong>Directions:</strong> " + e.Directions + "<br><br><strong>Question:</strong> <span id='quest'>" + e.Question + "</span><br><br><strong>Answers:</strong><br><br></div>");
    var answers = [];
    for(var i = 0; i < ans.length; i++){
        answers.push(ans[i].Answers);
    }
    for(var i = 0; i < answers.length; i++){
        $("#first").append("<span class='answers'>" + answers[i] + "</span><br/><br/>");
    }
    var parsing = true;
    var responses = "";
    var correct = "";
    for(var i = 0; i < e.Stats.length; i++){
        if(e.Stats[i] === "r"){
            parsing = false;
        }else{
            if(parsing){
                responses += e.Stats[i];
            }
        }
    }
    for(var i = 0; i < e.Stats.length; i++){
        if(e.Stats[i] === "\n"){
            parsing = true;
        }
        
        if(e.Stats[i] === "%"){
            parsing = false;
        }
        
        if(parsing){
            correct += e.Stats[i];
        }
    }
    
    correct = parseInt(correct);
    var numCorrect = parseFloat("0." + correct);
    var origResp = responses;
    responses = parseInt(responses.split(",").join(""));
    numCorrect = numeral(Math.ceil(responses * numCorrect)).format('0,0');
    
    $("#stats").append("<p>" + origResp + " people have attempted this question and approximately " + numCorrect + " (" + correct + "%) of them have gotten it right." + "<div id='disclaimer'>SAT is a registered trademark of the College Board and all content on this page is its sole property.</div>");
    $("#stats_button").click(function(){
        $("stats").fadeIn();
    });
}
