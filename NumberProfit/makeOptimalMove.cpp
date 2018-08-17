#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

float ownedByMe(vector<int> board, int boardPosition, int myPosition) {

  /* base case, we're on the spot */
  if (boardPosition == myPosition) {
	  return 1;
  }

  /* other base case, someone else is on the spot */
  if ((board.at(boardPosition) == 1) && (boardPosition != myPosition)) {
	  return 0;
  }
  board.at(myPosition) = 1;
  /* identify which spaces have tokens */

  for (int i = 1; i < board.size(); i++) {
  	/* if within board: */
	  int lower = 0;
  	int higher = 0;
	  if ((boardPosition - i) >= 0) {
	    lower = board.at(boardPosition - i);
  	}
  	if ((boardPosition + i) < board.size()) {
  	  higher = board.at(boardPosition + i);
  	}
  	/* check for a tie */
  	if ((lower == 1) && (higher == 1)) {
  	  if (((boardPosition - i) == myPosition) || ((boardPosition + i) == myPosition)) {
  	    return 0.5;
  	  } else {
  		return 0;
  	  }
  	} else {
  	  if (lower == 1) {
  		if ((boardPosition - i) == myPosition) {
  		  return 1;
  		} else {
  		  return 0;
  		  }
  	  } else if (higher == 1){
  		if ((boardPosition + i) == myPosition) {
    		  return 1;
    		} else {
    		  return 0;
    		  }
        }
  	  }
    }

  return 0;

}

float calculateProfit(vector<int> board, int tokenPosition) {

  float profit = 0;
  for (int i = 0; i < board.size(); i++) {
	  float owned = ownedByMe(board, i, tokenPosition);
	  profit += (i + 1) * owned;
    }
  return profit;

}

vector<int> makeOptimalFirstMove(vector<int> board, int nPlayers) {

  float maxProfit = 0;
  int maxIndex = 0;

  if (nPlayers == 0) {
	  for (int i = 0; i < board.size(); i++) {
	    if (board.at(i) == 0) {
	      float profit = calculateProfit(board, i);
	      if (profit > maxProfit) {
	        maxProfit = profit;
	  	    maxIndex = i;
	    	}
	    }
	  }
    board.at(maxIndex) = 1;
    return board;

  } else {
    for (int i = 0; i < board.size(); i++) {
      vector<int> hypoBoard = board;
      if (board.at(i) == 0) {
        hypoBoard.at(i) = 1;
        hypoBoard = makeOptimalFirstMove(hypoBoard, nPlayers -1);
        float profit = calculateProfit(hypoBoard, i);
        if (profit > maxProfit) {
          maxProfit = profit;
          maxIndex = i;
        }
      }
    }
    board.at(maxIndex) = 1;
    cout << "Optimal move with " << nPlayers << " players left is " << maxIndex + 1 << "\n";
    return board;
  }
}

int main() {

  int players;
  int spaces;
  cout << "How many players? ";
  cin >> players;
  cout << "How many spaces? ";
  cin >> spaces;

  vector<int> gameBoard;

  for (int i = 0; i < spaces; i++) {
	gameBoard.push_back(0);
  }
  /*
  for (int i = 0; i < players; i++) {
	int space;
	bool valid = false;
	do {
	  cout << "Pick a position for player " << i + 1 <<": ";
	  cin >> space;
	  space--;
	  if ((space < 0) || (space >= gameBoard.size())) {
		cerr << "Out of bounds! Pick a position between 1 and " << gameBoard.size() << "\n";
	  } else if (gameBoard.at(space) == 1){
		cerr << "Position " << space << " is already occupied. Try again.\n";
	  }
	  else {
		gameBoard.at(space) = 1;
		valid = true;
	  }
    } while (!valid);
  }
  */

  cout << makeOptimalFirstMove(gameBoard, players).at(0);

  return 0;
}
