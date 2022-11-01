using System;

public class Solution
{
    public static string solution(int a, int b)
    {
        DateTime dateValue = new DateTime(2016, a, b);
        return dateValue.DayOfWeek.ToString();
    }

    static void Main(string[] args)
    {
        Console.WriteLine(solution(5, 24));
    }
}