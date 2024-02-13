defmodule Solution do
  @spec first_palindrome(words :: [String.t()]) :: String.t()
  def first_palindrome(words) do
    words
    |> Enum.find("", &Solution.palindrome?/1)
  end

  @spec palindrome?(string :: String.t()) :: boolean()
  def palindrome?(string) do
    string == String.reverse(string)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test palindrome?" do
    assert Solution.palindrome?("aba") == true
    assert Solution.palindrome?("abba") == true
    assert Solution.palindrome?("abc") == false
  end

  test "test first_palindrome" do
    assert Solution.first_palindrome(["abc", "car", "ada", "racecar", "cool"]) == "ada"
    assert Solution.first_palindrome(["notapalindrome", "racecar"]) == "racecar"
    assert Solution.first_palindrome(["def", "ghi"]) == ""
  end
end
