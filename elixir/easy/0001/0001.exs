defmodule Solution do
  @spec two_sum(nums :: [integer], target :: integer) :: [integer]
  def two_sum(nums, target) do
    nums_indexed = Enum.with_index(nums)

    result =
      for x <- nums_indexed,
          y <- nums_indexed,
          elem(x, 1) < elem(y, 1) and elem(x, 0) + elem(y, 0) == target,
          do: [elem(x, 1), elem(y, 1)]

    [head | tail] = result
    head
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.two_sum([2, 7, 11, 15], 9) == [0, 1]
  end

  test "test_2" do
    assert Solution.two_sum([3, 2, 4], 6) == [1, 2]
  end

  test "test_3" do
    assert Solution.two_sum([3, 3], 6) == [0, 1]
  end
end
