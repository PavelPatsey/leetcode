defmodule Solution do
  @code_point_a ?a

  @spec group_anagrams(strs :: [String.t()]) :: [[String.t()]]
  def group_anagrams(strs) do
    get_map(%{}, strs)
    |> Map.values()
  end

  defp get_map(map, []) do
    map
  end

  defp get_map(map, [head | tail]) do
    key = get_signature(head)

    {_, new_map} =
      Map.get_and_update(map, key, fn current_value ->
        {current_value, if(current_value == nil, do: [head], else: [head | current_value])}
      end)

    get_map(new_map, tail)
  end

  @spec get_signature(str :: String.t()) :: {integer()}
  def get_signature(str) do
    counter =
      List.duplicate(0, 26)
      |> List.to_tuple()

    converted_str = get_converted(str)
    count(counter, converted_str)
  end

  @spec get_converted(str :: String.t()) :: [integer()]
  def get_converted(str) do
    String.to_charlist(str)
    |> Enum.map(fn x -> x - @code_point_a end)
  end

  defp count(counter, []) do
    counter
  end

  defp count(counter, [index | tail]) do
    count(put_elem(counter, index, elem(counter, index) + 1), tail)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "group_anagrams 1" do
    assert Solution.group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [
             ["nat", "tan"],
             ["ate", "tea", "eat"],
             ["bat"]
           ]
  end

  test "group_anagrams 2" do
    assert Solution.group_anagrams([""]) == [[""]]
  end

  test "group_anagrams 3" do
    assert Solution.group_anagrams(["a"]) == [["a"]]
  end

  test "get_converted 1" do
    assert Solution.get_converted("aaa") == [0, 0, 0]
  end

  test "get_converted 2" do
    assert Solution.get_converted("abz") == [0, 1, 25]
  end

  test "get_signature 1" do
    assert Solution.get_signature("aaa") == {
             3,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0
           }
  end

  test "get_signature 2" do
    assert Solution.get_signature("aabz") == {
             2,
             1,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             0,
             1
           }
  end
end
