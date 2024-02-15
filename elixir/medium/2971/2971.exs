defmodule Solution do
  @spec largest_perimeter(nums :: [integer]) :: integer
  def largest_perimeter(nums) do
    sorted_nums =
      nums
      |> Enum.sort()

    do_largest_perimeter(sorted_nums, 0, -1)
    |> IO.inspect()
  end

  def do_largest_perimeter([], _acc, result), do: result

  def do_largest_perimeter([head | tail], acc, result) when acc > head do
    do_largest_perimeter(tail, acc + head, acc + head)
  end

  def do_largest_perimeter([head | tail], acc, result) do
    do_largest_perimeter(tail, acc + head, result)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test largest_perimeter" do
    assert Solution.largest_perimeter([5, 5, 5]) == 15
    assert Solution.largest_perimeter([1, 12, 1, 2, 5, 50, 3]) == 12
    assert Solution.largest_perimeter([5, 5, 50]) == -1
  end
end
