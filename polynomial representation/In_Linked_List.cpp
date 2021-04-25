#include <iostream>
#include <string>

using namespace std;

struct node {
  int coefficient;
  int exponent;
  node *next;
};

class equation {
  node *start;

 public:
  equation() { start = nullptr; }

  void add_term(char *term) {
    try {
    } catch (exception &e) {
      cout << e.what() << '\n';
    }
  }
};

int main() {
  int degree;
  char expr[100];
  int no_of_terms;
  cout << "Enter total no of terms - ";
  cin >> no_of_terms;
  cout << "Enter polynomial in format such that every term consist of \' "
          "[coefficient][variable][degree]+[coefficient][variable][degree]+ so "
          "on .......\'  Also note that there should not be any space between "
          "the consecutive terms - ";
  cin >> expr;
  // cout<<expr ;

  equation polynomial;

  for (int i = 0; expr[i] != '\0'; i += 3) {
    switch (expr[i]) {
      case '+':
        continue;
        break;

      default:
        char *term = new char[3];
        term[0] = expr[i];
        term[1] = expr[i + 1];
        term[2] = expr[i + 2];
        polynomial.add_term(term);
        break;
    }
  }

  return 0;
}
