defmodule Solution do
  @spec majority_element(nums :: [integer]) :: integer
  def majority_element(nums) do
    do_majority_element(nums, 0, 0)
  end

  def do_majority_element([], _count, result), do: result

  def do_majority_element([head | tail], count = 0, _result) do
    do_majority_element(tail, count + 1, head)
  end

  def do_majority_element([result | tail], count, result) do
    do_majority_element(tail, count + 1, result)
  end

  def do_majority_element([_head | tail], count, result) do
    do_majority_element(tail, count - 1, result)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.majority_element([3, 2, 3]) == 3
  end

  test "test_2" do
    assert Solution.majority_element([2,2,1,1,1,2,2]) == 2
  end
end
