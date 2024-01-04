defmodule Solution do
  @spec min_operations(nums :: [integer]) :: integer
  def min_operations(nums) do
    values =
      nums
      |> Enum.frequencies()
      |> Map.values()

    if 1 in values do
      -1
    else
      values
      |> Enum.map(fn x -> div(x, 3) + boolean_to_integer(rem(x, 3) != 0) end)
      |> Enum.sum()
    end
  end

  def boolean_to_integer(bool) do
    if bool, do: 1, else: 0
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.min_operations([2, 3, 3, 2, 2, 4, 2, 3, 4]) == 4
  end

  test "test_2" do
    assert Solution.min_operations([2, 1, 2, 2, 3, 3]) == -1
  end

  test "test_3" do
    assert Solution.min_operations([16, 16, 16, 19, 16, 3, 16, 8, 16, 16, 16, 19, 3, 16, 16]) ==
             -1
  end
end
