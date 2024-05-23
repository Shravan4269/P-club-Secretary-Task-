# Solution
Let's go step by step 

 1. For k =1 to n it is easy to see that if Iron Man just open alternate cards only he can have a easy win
 2. For k = n+1 we need to have at least one pair of cards opened to achieve this strategy is Ex- [1,2,3,4,5,6,7,8,9] n = 4 and k = 5
     Here , move sequence I = 1 , C = 0 ;I = 3 , C = 0 ;I = 2 , C = 1;I = 5 , C = 0;I = 7 , C = 0;I = 9 , C = 0; 
     Note - Here Captain on third round can turn 3 off also but then Iron man will go like 4,6,8
 3. For k >n+1 Captain can follow simple strategy whenever Ironman try to open a~2i~ and a~2i-1~ , &forall; i $\in$ [1,n], card together he will close any one and always have no. of opened card less than n+1.
 4. Now number of rounds here equals to K + [no. of cards closed by Captain] so for minimum moves in k =1 to n are k only while for k = n+1 is k+1 as we see above.
 5. Now for k = 1 to n Iron Man can choose any k non consecutive cards and he will win while for k = n+1 the final sequence will have atleast and atmost one pair of cards opened together.
 6. So for k = 1 to n ans is ^2n-k^C~k-1~ $\times$ $(2n+1)/k$ (mathematical result for choosing k non consecutive points in circle) and for k = n+1 ans is 2n+1 only.
 7. Now it is easy to write solution except the part where Combitorial expression is to calculated.
 8. For that we can make a storing array of 1 to n! mod p in factorial_array[n+1] and modular inverse of 1 to n! mod p in inverse_factorial[n+1] and then use them in any query 
 9. Time complexity will be O(n$\cdot$logp) 


Code:
// initialization

    #include <bits/stdc++.h>
    #define ll long long
    const int N = 1000001;
    using namespace std;
    // array to store inverse of 1 to N
    ll factorialNumInverse[N + 1];
    // array to precompute inverse of 1! to N!
    ll naturalNumInverse[N + 1];
    // array to store factorial of first N numbers
    ll fact[N + 1];


// Function to precompute inverse of numbers

    void InverseofNumber(ll p)
    {
        naturalNumInverse[0] = naturalNumInverse[1] = 1;
        for (int i = 2; i <= N; i++)
            naturalNumInverse[i] = naturalNumInverse[p % i] * (p - p / i) % p;
    }

// Function to precompute inverse of factorials

    void InverseofFactorial(ll p)
    {
        factorialNumInverse[0] = factorialNumInverse[1] = 1;
     
        // precompute inverse of natural numbers
        for (int i = 2; i <= N; i++)
            factorialNumInverse[i] = (naturalNumInverse[i] * factorialNumInverse[i - 1]) % p;
    }
 
// Function to calculate factorial of 1 to N

    void factorial(ll p)
    {    
        fact[0] = 1;
     
        // precompute factorials
        for (int i = 1; i <= N; i++) {
            fact[i] = (fact[i - 1] * i) % p;
        }
    }
 
// Function to return nCr % p in O(1) time

    ll Binomial(ll N, ll R, ll p){   
    // n C r = n!*inverse(r!)*inverse((n-r)!)
    ll ans = ((fact[N] * factorialNumInverse[R])
              % p * factorialNumInverse[N - R])
             % p;
    return ans;
    }
 
// Driver Code


    int main()
    {
      // Calling functions to precompute the
      // required arrays which will be required
      // to answer every query in O(1)
      ll p = 1000000007;
      InverseofNumber(p);
      InverseofFactorial(p);
      factorial(p);
      
      ll t;
      cin >> t;
      while(t--){
          ll n,k;
          cin >> n >> k;
          if(k>n+1){
              cout << "No" <<endl;
          }
          else{
              cout << "Yes" <<endl;
              if(k==n+1){
                  cout << k+1 <<" " << 2*n+1<<endl;
              }
              else {
                  ll ans = Binomial(2*n-k,k-1,p);
                  ans = (((ans*(2*n+1))%p)*naturalNumInverse[k])%p;
                  cout << k <<" " << ans<<endl;
              }
          }
      }
      return 0;
    }


