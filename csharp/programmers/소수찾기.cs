using System;
using System.Linq;

public class Solution
{
    public int solution(int n)
    {
        int answer = 0;
        bool[] arr = Enumerable.Repeat(true, n + 1).ToArray();
        arr[0] = false;
        arr[1] = false;


        for (int i = 2; i <= Math.Sqrt(n); i++)
        {
            if (arr[i] == true)
            {
                for (int j = i + i; j < n + 1; j = j + i)
                {
                    arr[j] = false;
                }
            }
        }
        answer = arr.Count(s => s == true);
        return answer;
    }
}