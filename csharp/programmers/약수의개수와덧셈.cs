using System;

public class Solution
{
    static int solution(int left,int right) {
        int sum = 0;
        for(int i = left; i <= right; i++)
        {
            int count = 0;
            for(int j = 1; j <= i; j++)
            {
                if (i % j == 0) count += 1;
            }
            if (count % 2 == 0) sum += i;
            else sum -= i;
        }
        return sum;
        
    }
    static void Main(string[] args)
    {
        Console.WriteLine(solution(13, 17));
    }
}
