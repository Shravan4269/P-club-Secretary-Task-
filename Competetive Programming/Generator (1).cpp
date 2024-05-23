#include "testlib.h"
#include <iostream>
using namespace std;
int main(int argc, char* argv[]) {
    registerGen(argc, argv, 1);
    int N = 500000;
    int t = rnd.next(1,100000);
    cout << t <<endl;
    for(int i=0;i<t;i++){
        int k = rnd.next(2, N);
        cout << k <<" ";
        println(rnd.next(1,2*k+1));
    }
}