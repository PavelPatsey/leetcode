defmodule Solution do
  @spec find_content_children(g :: [integer], s :: [integer]) :: integer
  def find_content_children(g, s) do
    g = Enum.sort(g)
    s = Enum.sort(s)
    _find_content_children(g, s, 0)
  end

  defp _find_content_children([head_g | tail_g], [head_s | tail_s], accumulator)
       when head_g <= head_s do
    _find_content_children(tail_g, tail_s, accumulator + 1)
  end

  defp _find_content_children(g, [_head_s | tail_s], accumulator) do
    _find_content_children(g, tail_s, accumulator)
  end

  defp _find_content_children(_g, [], accumulator) do
    accumulator
  end

  defp _find_content_children([], _s, accumulator) do
    accumulator
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.find_content_children([1, 2, 3], [1, 1]) == 1
  end

  test "test_2" do
    assert Solution.find_content_children([1, 2], [1, 2, 3]) == 2
  end

  test "test_3" do
    assert Solution.find_content_children([10, 9, 8, 7], [5, 6, 7, 8]) == 2
  end
end
