#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int calcan(int number, int loc)
{
    int can = 0;
    if (number == 0)
        number = 11;
    if (loc == 0)
        loc = 11;
    if (number > loc)
    {
        if (number - loc >= 3)
        {
            can += (number - loc) / 3;
            can += (number - loc) % 3;
        }
        else
            can = number - loc;
    }
    else if (number < loc)
    {
        if (loc - number >= 3)
        {
            can += (loc - number) / 3;
            can += (loc - number) % 3;
        }
        else
            can = loc - number;
    }
    else if (number == loc)
    {
        return can;
    }
    return can;
}

string solution(vector<int> numbers, string hand)
{
    string answer = "";
    int lhl = 10, rhl = 12;

    for (int i = 0; i < numbers.size(); i++)
    {
        if (numbers[i] == 1 || numbers[i] == 4 || numbers[i] == 7)
        {
            answer += "L";
            lhl = numbers[i];
        }
        else if (numbers[i] == 3 || numbers[i] == 6 || numbers[i] == 9)
        {
            answer += "R";
            rhl = numbers[i];
        }
        else
        {
            if (calcan(numbers[i], lhl) == calcan(numbers[i], rhl))
            {
                answer += toupper(hand[0]);
                if (hand == "left")
                    lhl = numbers[i];
                else
                    rhl = numbers[i];
            }
            else if (calcan(numbers[i], lhl) > calcan(numbers[i], rhl))
            {
                answer += "R";
                rhl = numbers[i];
            }
            else if (calcan(numbers[i], lhl) < calcan(numbers[i], rhl))
            {
                answer += "L";
                lhl = numbers[i];
            }
        }
    }
    return answer;
}