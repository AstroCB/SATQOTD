var req = new XMLHttpRequest();
  req.open('GET', 'http://www.kimonolabs.com/api/a9tmzsfm?apikey=74ef20963a82fa61fe92928fd750f7ce', true);
  req.onload = function(e) {
      if(req.readyState === 4 && req.status == 200) {
        var results = JSON.parse(req.responseText);
        console.log("                   ----" + results.name + "----");
		console.log("----Last updated: " + results.lastsuccess + "----\n");

		results = results.results;
		var qresults = results['Question Data'];
		var first_results = qresults[0];

		var date = first_results['Date'];
		var directions = first_results.Directions;


		var second_results = qresults[1];
		var stats = second_results.Stats;

		var third_results = qresults[2];
		var typeques = third_results['Type of Question'];
		var question = third_results.Question;
		var tries = "";
		var percent = "";

		var checking = true;
		var i = 0;
        var x = 0;

		while(checking){
            x = stats[i];
			if(x !== " "){
				tries += x;
			}else{
				checking = false;
			}
			i++;
		}

		checking = true;
		var now_checking = false;

		i = 0;
        x = 0;
		var y = 0;

		while(checking){ //This gets a bit complicated; the data I'm parsing reads "xx,xxx responses \nxx% correct"; I'm looking for the 'xx%', so I want to start adding to percent if it's after \n and stop at the space after the '%'; probably a better way to do this
			for(x in stats){
				if(x === "\n" && y > 0){
					now_checking = true;
				}else if(x === "\n"){
					y += 1;
				}
				if(now_checking){
					if(x === " "){
						now_checking = false;
						checking = false;
					}
					if(now_checking){
						percent += x;
					}
				}
			}
		}

        x = 0;

		var temp = "";

		percent = percent.split();

		for(i in percent){
			if(i !== " " && i !== "\n"){
				temp += i;
			}
		}

		percent = temp.toString();


		temp = "";

		for(x in date){
			if(x !== "\n"){
				temp += x;
			}else{
				temp += " ";
			}
		}

		date = temp;



		console.log("Hello. Welcome to your daily SAT training. Today is " + date + ". Your mission, should you choose to accept it, will be to answer this question, which is classified as: " + typeques + ".\n");
		console.log("Warning. This mission is dangerous. " + tries + " people have tried and " + percent + " of them have survived (okay, gotten it correct).\n");
		console.log("Here is your briefing: \n" + directions);

		var validans = false;
		var resp = true;

		/*while(!validans){
			var start = alert("Ready to begin? Type 'yes' or 'no'.");
			start = start.toUpperCase();
			if(start === 'YES'){
				validans = true;
				resp = true;
			}else if(start === 'NO'){
				validans = true;
				resp = false;
			}else{
				console.log("Sorry. Try again:\n");
			}
		}*/


		if(resp === true){
			console.log(question);
			var aresults = results["Answer Data"];
			for(i in aresults){
				console.log(i.Answers);
			}
		}
	}
};

req.onload();
