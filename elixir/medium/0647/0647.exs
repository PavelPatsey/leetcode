defmodule Solution do
  @spec count_substrings(s :: String.t()) :: integer
  def count_substrings(s) do
    tuple_s =
      s
      |> String.graphemes()
      |> List.to_tuple()

    get_count(tuple_s, 0, 0)
  end

  def get_count(tuple_s, count, i) when i >= tuple_size(tuple_s) do
    count
  end

  def get_count(tuple_s, count, i) do
    left = right = i
    count = count + while(tuple_s, 0, i, left, right)

    left = i
    right = i + 1
    count = count + while(tuple_s, 0, i, left, right)

    get_count(tuple_s, count, i + 1)
  end

  def while(tuple_s, acc, _i, left, right) when left < 0 or right >= tuple_size(tuple_s) do
    acc
  end

  def while(tuple_s, acc, i, left, right) do
    if elem(tuple_s, left) == elem(tuple_s, right) do
      while(tuple_s, acc + 1, i, left - 1, right + 1)
    else
      acc
    end
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.count_substrings("abc") == 3
  end

  test "test_2" do
    assert Solution.count_substrings("aaa") == 6
  end
end
