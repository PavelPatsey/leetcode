defmodule Solution do
  @spec halves_are_alike(s :: String.t()) :: boolean
  def halves_are_alike(s) do
    [a, b] =
      String.split_at(s, div(String.length(s), 2))
      |> Tuple.to_list()
      |> Enum.map(&Solution.get_vowels_count/1)

    a == b
  end

  @spec get_vowels_count(string :: String.t()) :: Integer
  def get_vowels_count(string) do
    vowels_set =
      String.to_charlist("aeiouAEIOU")
      |> MapSet.new()

    string
    |> String.to_charlist()
    |> Enum.filter(fn x -> x in vowels_set end)
    |> length()
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test get_vowels_count" do
    assert Solution.get_vowels_count("book") == 2
  end

  test "test_1" do
    assert Solution.halves_are_alike("book") == true
  end

  test "test_2" do
    assert Solution.halves_are_alike("textbook") == false
  end
end
