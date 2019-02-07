#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <queue>
#include <set>

using namespace std;

vector<string> tokenize_input(string input)
{
    vector<string> inputs;
    size_t pos = 0;
    string token;
    while ((pos = input.find(" ")) != string::npos)
    {
        token = input.substr(0, pos);
        inputs.push_back(token);
        input.erase(0, pos + 1);
    }
    return inputs;
}

vector<int> to_digit_vector(string input)
{
    vector<int> digits;
    for (auto i = 0; i < input.size(); i++)
    {
        int digit = input.at(i) - '0';
        digits.push_back(digit);
    }
    return digits;
}

int main()
{
    string input;
    cin >> input;

    vector<string> inputs = tokenize_input(input);
    int r = stoi(inputs[0], nullptr);
    int c = stoi(inputs[1], nullptr);

    vector<vector<int>> grid;

    for (auto i = 0; i < r; i++)
    {
        cin >> input;
        vector<int> row = to_digit_vector(input);
        grid.push_back(row);
    }

    cin >> input;
    int n = stoi(input, nullptr);

    for (auto i = 0; i < n; i++)
    {
        cin >> input;
        vector<string> inputs = tokenize_input(input);
        vector<int> input_numbers;

        for (auto token : inputs)
        {
            input_numbers.push_back(stoi(token) - 1);
        }

        pair<int, int> pos1, pos2;
        pos1.first = input_numbers[0];
        pos1.second = input_numbers[1];
        pos2.first = input_numbers[2];
        pos2.second = input_numbers[3];

        int person_type = grid[pos1.first][pos1.second];
        string type_string = (person_type == 0) ? "binary" : "decimal";

        // Breadth-First search to check if a path exists between pos1 and pos2.
        queue<pair<int, int>> q;
        set<pair<int, int>> visited;
        q.push(pos1);
        visited.insert(pos1);
        bool path_exists = false;

        while (!q.empty())
        {
            pair<int, int> cell = q.front();
            q.pop();

            if (cell.first == pos2.first && cell.second == pos2.second)
            {
                path_exists = true;
                break;
            }

            pair<int, int> up, down, left, right;
            up.first = cell.first - 1;
            up.second = cell.second;
            down.first = cell.first + 1;
            down.second = cell.second;
            left.first = cell.first;
            left.second = cell.second - 1;
            right.first = cell.first;
            right.second = cell.second + 1;

            vector<pair<int, int>> candidates;
            candidates.push_back(up);
            candidates.push_back(down);
            candidates.push_back(left);
            candidates.push_back(right);

            for (auto candidate : candidates)
            {
                int cand_r = candidate.first;
                int cand_c = candidate.second;

                if (cand_r >= 0 && cand_r < r && cand_c >= 0 && cand_c < c)
                {
                    if (grid[cand_r][cand_c] == person_type && visited.find(candidate) == visited.end())
                    {
                        q.push(candidate);
                        visited.insert(candidate);
                    }
                }
            }
        }

        string output = path_exists ? type_string : "neither";
        cout << output << endl;
    }

    return 0;
}