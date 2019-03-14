#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

class Solution
{
    public:
    int numJewelsInStones(string J, string S)
    {
        unordered_set<char> jewels;
        for (char c : J)
            jewels.insert(c);
        int count = 0;
        for (char c : S)
        {
            if (jewels.find(c) != jewels.end())
                count++;
        }
        return count;
    }
};

int main()
{
    Solution sol;
    cout << sol.numJewelsInStones("aA", "aAAbbbb") << endl;
    return 0;
};