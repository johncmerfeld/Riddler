
#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
using namespace std;

/* Get the ownership relationship to a space on the board

  arguments: board - a vector of ints representing the stacks
             boardPosition - an int, which index of the board to examine
             myPosition - an int, from where on the board is the ownership assessed
  returns: a float, one of {1 - I own it fully
                            0.5 - I own half of it
                            0 - I don't own it at all}
*/
float ownedByMe(vector<int> board, int boardPosition, int myPosition) {

  /* base case, we're on the spot */
  if (boardPosition == myPosition) {
	  return 1;
  }

  /* other base case, someone else is on the spot */
  if ((board.at(boardPosition) == 1) && (boardPosition != myPosition)) {
	  return 0;
  }
  /* mark myPosition since it's a hypothetical spot as of now */
  board.at(myPosition) = 1;

  /* start searching outward from the position in question */
  for (int i = 1; i < board.size(); i++) {
	  int lower = 0;
  	int higher = 0;
    /* check if within board */
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

/* calculate the profitability of a board from a position
  arguments: board - a vector of ints representing the stacks
             tokenPosition - an int, which index of the board to base profit on
*/
float calculateProfit(vector<int> board, int tokenPosition) {

  float profit = 0;
  for (int i = 0; i < board.size(); i++) {
	  float owned = ownedByMe(board, i, tokenPosition);
	  profit += (i + 1) * owned;
    }
  return profit;
}

/* find the most profitable move given opponants' optimal moves
  arguments: board - a vector of ints representing the stacks
             nPlayers - int, how many more players are left, including me
*/
vector<int> makeOptimalMove(vector<int> board, int nPlayers) {

  float maxProfit = 0;
  int maxIndex = 0;
  vector<int> optimalHypoBoard;

  /* base case, find best spot on the current board */
  if (nPlayers <= 1) {
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

  /* find best spot assuming next player will make an optimal move */
  } else {
    for (int i = 0; i < board.size(); i++) {
      vector<int> hypoBoard = board;
      if (board.at(i) == 0) {
        hypoBoard.at(i) = 1;
        hypoBoard = makeOptimalMove(hypoBoard, nPlayers - 1);
        float profit = calculateProfit(hypoBoard, i);
        if (profit > maxProfit) {
          optimalHypoBoard = hypoBoard;
          maxProfit = profit;
          maxIndex = i;
        }
      }
    }
    board = optimalHypoBoard;
    return board;
  }
}

/* find the most profitable first move given opponants' optimal moves
  arguments: board - a vector of ints representing the stacks
             nPlayers - int, how many more players are left, including me
*/
vector<int> makeOptimalFirstMove(vector<int> board, int nPlayers) {

  float maxProfit = 0;
  int maxIndex = 0;
  /* find best spot assuming next player will make an optimal move */
  for (int i = 0; i < board.size(); i++) {
    vector<int> hypoBoard = board;
    if (board.at(i) == 0) {
      hypoBoard.at(i) = 1;
      hypoBoard = makeOptimalMove(hypoBoard, nPlayers - 1);
      float profit = calculateProfit(hypoBoard, i);
      if (profit > maxProfit) {
        maxProfit = profit;
        maxIndex = i;
      }
    }
  }
  board.at(maxIndex) = 1;
  return board;
}

int main() {

  /* read in game information */
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

  /* record information about first move */
  vector<int> optimalBoard = gameBoard;
  int firstMoveIndex = 0;
  for (int i = 0; i < players; i++) {
    optimalBoard = makeOptimalFirstMove(optimalBoard, players - i);
    if (i == 0) {
      for (int j = 0; j < optimalBoard.size(); j++) {
        if (optimalBoard.at(j) == 1) {
          firstMoveIndex = j;
        }
      }
    }
  }

  /* generate summary statistics */
  float firstMoveProfit = calculateProfit(optimalBoard, firstMoveIndex);
  float total = 0;
  float avg = 0;
  float allMoney = 0;

  for (int i = 0; i < optimalBoard.size(); i++) {
    if ((optimalBoard.at(i) == 1) && (i != firstMoveIndex)) {
      total += calculateProfit(optimalBoard, i);
    }
    allMoney += (i+1);
  }
  avg = total / (players - 1);

  optimalBoard.at(firstMoveIndex) = 11;

  cout << "Optimal game board shown below (first move marked '11')\n";
  for (int i = 0; i < optimalBoard.size(); i++) {
    cout << i + 1 << ". " << optimalBoard.at(i) << "\n";
  }

  cout << "Optimal first move is " << firstMoveIndex + 1 << " with profit $" << setprecision (2) << fixed << firstMoveProfit << " (" << ((firstMoveProfit/allMoney) * 100) << "% of the total money)" "\n";
  cout << "Average profit for non-first moves is $" << setprecision (2) << fixed << avg << "\n";
  cout << "Advantage of moving first is $" << setprecision (2) << fixed << firstMoveProfit - avg << "\n";


  return 0;
}
