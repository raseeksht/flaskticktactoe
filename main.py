from flask import Flask,render_template,request,redirect

app = Flask(__name__)


whoseTurn = 1

@app.route("/",methods=["GET","POST"])
def index():
	if request.method == "POST":
		names = request.form
		global players
		global userSymbol
		player1  = names["player1"]
		player2  = names["player2"]
		players = {"player1":player1,"player2":player2}
		userSymbol = {"player1":"X","player2":"O"}
		return redirect("/play")

	return render_template("getname.html")


@app.route("/play")
def play():
	return render_template("play.html",players=players,userSymbol=userSymbol)

@app.route("/getturn",methods=["GET"])
def getTurn():

	return str(whoseTurn)


def whoIsWinner(pos,players,userSymbol):
	print("postion is: ",pos,"\n")
	if (pos == userSymbol['player1']):
		print("player1 chai winner ho",players['player1'])
		return f'{players["player1"]} is the winner'
		print("aba execure hudaina")
	else:
		print("player2 chai winner ho")
		return f'{players["player2"]} is the winner'



def checkWinner(board,players,userSymbol):
	ox = [userSymbol["player1"],userSymbol["player2"]]
	if (board["top-L"] == board["top-M"] == board["top-R"] in ox):
		return whoIsWinner(board["top-L"],players,userSymbol)

	elif (board["mid-L"] == board["mid-M"] == board["mid-R"] in ox):
		return whoIsWinner(board["mid-L"],players,userSymbol)

	elif(board["low-L"] == board["low-M"] ==board["low-R"] in ox):
		return whoIsWinner(board["low-L"],players,userSymbol)
	
	elif (board["low-L"] == board["mid-M"] == board["top-R"] in ox):
		return whoIsWinner(board["low-L"],players,userSymbol)

	elif (board["top-L"] == board["mid-M"] == board["low-R"] in ox):
		return whoIsWinner(board["top-L"],players,userSymbol)

	elif (board["top-L"] == board["mid-L"] == board["low-L"] in ox):
		return whoIsWinner(board["top-L"],players,userSymbol)

	elif (board["top-M"] == board["mid-M"] == board["low-M"] in ox):
		return whoIsWinner(board["top-M"],players,userSymbol)

	elif (board["top-R"] == board["mid-R"] == board["low-R"] in ox):
		return whoIsWinner(board["top-R"],players,userSymbol)
	else:
		# if nothing happens
		return


def reset():
	global board
	global availableMoves
	board ={"top-L": " ","top-M":" ","top-R": " ",
			"mid-L": " ","mid-M":" ","mid-R": " ",
			"low-L": " ","low-M":" ","low-R": " "
		}
	availableMoves =["top-L","top-R","top-M","mid-L","mid-M","mid-R","low-L","low-R","low-M"]

reset()
#unused piece of code
class players:
	"""docstring for players"""
	def __init__(self, player1,player2):		
		self.player1 = player1
		self.player2 = player2
		self.player1Sym = 'X'
		self.player2Sym = 'O'
		


def verifyWinner(board,players,userSymbol):
	winner = checkWinner(board,players,userSymbol)
	if winner:
		return winner

@app.route('/move',methods=["POST"])
def move():
	move = request.form["move"]
	turn = request.form["turn"]
	global whoseTurn
	global board
	global players
	global availableMoves
	if move in availableMoves:
		availableMoves.remove(move)
		# print("available moves:", availableMoves)
	else:
		if int(turn) == 1:			
			return f"{players['player1']}'s turn (Invalid choice go again..)"
		else:
			return f"{players['player2']}'s turn (Invalid choice go again..)"

	if int(turn) == 1:
		board[move] = "X"
		print("\n\n\n")
		print(board)
		print("\n\n\n")

		whoseTurn = 2
		checker = verifyWinner(board,players,userSymbol)
		if (checker):
			return checker
		return f"""{players["player2"]}'s turn"""

	elif int(turn) == 2:
		board[move] = "O"
		print(board)
		
		whoseTurn = 1
		checker = verifyWinner(board,players,userSymbol)
		if checker:
			# return f'{players["player2"]} is winner'
			return checker
		return f"""{players["player1"]}'s turn"""
	if (len(availableMoves) == 0):
		return "Match Draw"
	

@app.route("/clearall",methods=["GET"])
def clearall():
	# global players
	# global board
	# global whoseTurn
	# players = {}
	# board = {}
	# whoseTurn = 1
	reset()
	return redirect("/")




@app.route("/playagain",methods=["GET"])
def playAgain():
	global players
	global userSymbol
	print(userSymbol)
	reset()
	return render_template("play.html",players=players,userSymbol=userSymbol)




if __name__ == '__main__':
	app.run(port="2020",debug=True)