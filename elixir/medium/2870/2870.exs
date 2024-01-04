defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    nums
    |> Enum.frequencies()
    |> IO.inspect()
    |> Map.values()
    |> IO.inspect()
  end

  def boolean_to_integer(bool) do
    if bool, do: 1, else: 0
  end
end

Solution.min_operations([2, 3, 3, 2, 2, 4, 2, 3, 4])

# ExUnit.start()

# defmodule AssertionTest do
#   use ExUnit.Case, async: true

#   test "test_1" do
#     assert Solution.min_operations([2, 3, 3, 2, 2, 4, 2, 3, 4]) == 4
#   end

#   test "test_2" do
#     assert Solution.min_operations([2, 1, 2, 2, 3, 3]) == -1
#   end
# end
