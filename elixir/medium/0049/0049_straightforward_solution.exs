defmodule Solution do
  @spec group_anagrams(strs :: [String.t()]) :: [[String.t()]]
  def group_anagrams(strs) do
    strs
    |> Enum.map(&{&1 |> String.to_charlist() |> Enum.frequencies(), &1})
    |> IO.inspect()
    |> Enum.group_by(&elem(&1, 0), &elem(&1, 1))
    |> IO.inspect()
    |> Map.values()
    |> IO.inspect()
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "group_anagrams 1" do
    assert Solution.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
             ["bat"],
             ["eat", "tea", "ate"],
             ["tan", "nat"]
           ]
  end

  # test "group_anagrams 2" do
  #   assert Solution.group_anagrams([""]) == [[""]]
  # end

  # test "group_anagrams 3" do
  #   assert Solution.group_anagrams(["a"]) == [["a"]]
  # end
end
