using System;

public class Solution
{
    public static string solution(int a, int b)
    {
        DateTime date = new DateTime(2016, a, b);
        return date.DayOfWeek.ToString().ToUpper().Substring(0, 3);
    }
}