#include <iostream>
using namespace std;
#include <vector>



vector<int> inserted_sort(vector<int>& L){
    if (L.capacity()<2){
        return L;
    }
    else{
        for (int i=1; i<L.capacity();i++){
            int key=L[i];
            int j=i-1;
            while (j>-1 & L[j]>key){
                L[j+1]=L[j];
                j--;
            }
            L[j+1]=key;
        }
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
inserted_sort(laguerre);
cout<<" the sorted list is ";
for(int i=0; i<laguerre.capacity();i++){
    cout<< laguerre[i] <<" ";
}
cout << endl;
}

