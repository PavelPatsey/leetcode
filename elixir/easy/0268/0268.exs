defmodule Solution do
  @spec missing_number(nums :: [integer]) :: integer
  def missing_number(nums) do
    n = length(nums)
    sum = div(n * (n + 1), 2)
    sum - Enum.sum(nums)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test missing_number" do
    assert Solution.missing_number([3, 0, 1]) == 2
    assert Solution.missing_number([0, 1]) == 2
    assert Solution.missing_number([9, 6, 4, 2, 3, 5, 7, 0, 1]) == 8
    assert Solution.missing_number([1]) == 0
    assert Solution.missing_number([1, 2]) == 0
  end
end
