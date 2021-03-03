#include <iostream>
using namespace std;
#include <vector>



vector<int> quick_sort(vector<int>& L){
    if (L.capacity()<2){
        return L;
    }
    else{
        vector<int> leftSide,rightSide;
        int m=L.capacity()/2;
        for (int i=1; i<L.capacity();i++){
            if(L[i]<L[m]){
                leftSide.push_back(L[i]);
            }
            else{
                rightSide.push_back(L[i]);
            }
        }
     vector<int> leftSorted=quick_sort(leftSide),rightSorted=quick_sort(rightSide);
      for (int i=0; i<rightSorted.capacity();i++){
          leftSorted.push_back(rightSorted[i]);
      }
      L=leftSorted;
      return L;
    }
}

int main(){

vector<int> laguerre={7,2,4,1,68,10,52};

cout<< " This program will sort the list  by using insertion technique"<< endl;
cout<<" the initial list is ";
for(int i=0; i<laguerre.capacity();i++){
    cout<< laguerre[i] <<" ";
}
cout << endl;
quick_sort(laguerre);
cout<<" the sorted list is ";
for(int i=0; i<laguerre.capacity();i++){
    cout<< laguerre[i] <<" ";
}
cout << endl;
}

