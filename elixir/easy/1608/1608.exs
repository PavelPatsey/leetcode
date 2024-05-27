

defmodule Solution do
  @spec special_array(nums :: [integer]) :: integer
  def special_array(nums) do
    len_nums = length(nums)
    do_special_array(0, len_nums, nums)
  end

  defp do_special_array(x, len_nums, _nums) when x > len_nums, do: -1

  defp do_special_array(x, len_nums, nums) do
    counter = get_counter(x, 0, nums)

    if counter == x do
      x
    else
      do_special_array(x + 1, len_nums, nums)
    end
  end

  defp get_counter(_x, counter, []), do: counter

  defp get_counter(x, counter, [head | tail]) do
    if head >= x do
      get_counter(x, counter + 1, tail)
    else
      get_counter(x, counter, tail)
    end
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "special_array" do
    assert Solution.special_array([3, 5]) == 2
    assert Solution.special_array([0, 0]) == -1
    assert Solution.special_array([0, 4, 3, 0, 4]) == 3
    assert Solution.special_array([3, 6, 7, 7, 0]) == -1
  end
end
