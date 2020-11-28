


function move(move){
	turn = $(".determineTurn").val()
	className = "."+move
	// $.get("/getturn",
	// function(data){
	// 	turn = data
	// 	console.log(turn+" ko palo")
	// })

	if (turn == '1'){
		$(className).html("X")
		$('.determineTurn').val("2")
	}else{
		$(className).html("O")
		$('.determineTurn').val("1")
	}
    
	$.post('/move',
	{
    	move:move,
    	turn:turn
	},
	function(data){  
		$(".turn").text(data)		

	})
}




