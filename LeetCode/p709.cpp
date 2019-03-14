#include <iostream>
#include <string>

using namespace std;

class Solution
{
    public:
        string toLowerCase(string str)
        {
            string lowered;
            for (char c : str)
            {
                if (c < 97 && c >= 65)
                    c += 32;
                lowered += c;
            }
            return lowered;
        }
};

int main()
{
    Solution sol;
    cout << sol.toLowerCase("Hallo") << endl;
    return 0;
}