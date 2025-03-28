#include<iostream>
#include<stack>
#include<string>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        int len = s.length();
        char c1, c2;
        if (len % 2 != 0){
          return false;
        }
        stack<char> st;
        for (int i=0; i<len; i++){
            if ((s[i] == 40) || (s[i] == 91) || (s[i] == 123)){
                st.push(s[i]);
            }
            else{
                if (st.empty()){return false;}
                char c = st.top();
                st.pop();
                if ((s[i] == ')' && c != '(') || (s[i] == ']' && c != '[') || ((s[i] == '}' && c != '{'))){return false;}
            }
        }
        return st.empty();
    }
};