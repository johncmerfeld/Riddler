#include <iostream>
#include <vector>
using namespace std;

float calculateProfit(vector<bool>* board, int nPlayersRemaining, int tokenPosition) {

  if (nPlayersRemaining == 0) {
    return(board->at(tokenPosition));

  }

}

int main() {

  int players;
  int spaces;
  cout << "How many players? ";
  cin >> players;
  cout << "How many spaces? ";
  cin >> spaces;

  vector<bool>* gameBoard = new vector<bool>(spaces, 0);

  cout << calculateProfit(gameBoard, 0, 5);

  return 0;
}
