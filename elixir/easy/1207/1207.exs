defmodule Solution do
  @spec unique_occurrences(arr :: [integer]) :: boolean
  def unique_occurrences(arr) do
    values =
      arr
      |> Enum.frequencies()
      |> Map.values()

    values == Enum.uniq(values)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.unique_occurrences([1, 2, 2, 1, 1, 3]) == true
  end

  test "test_2" do
    assert Solution.unique_occurrences([1, 2]) == false
  end
end
