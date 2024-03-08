defmodule Solution do
  @spec max_frequency_elements(nums :: [integer]) :: integer
  def max_frequency_elements(nums) do
    frequencies =
      nums
      |> Enum.frequencies()

    max_value =
      frequencies
      |> Map.values()
      |> Enum.max()

    frequencies
    |> Enum.filter(fn {_k, v} -> v == max_value end)
    |> Enum.map(fn {_k, v} -> v end)
    |> Enum.sum()
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test max_frequency_elements" do
    assert Solution.max_frequency_elements([1, 2, 2, 3, 1, 4]) == 4
    assert Solution.max_frequency_elements([1, 2, 3, 4, 5]) == 5
  end
end
