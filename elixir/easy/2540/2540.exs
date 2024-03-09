defmodule Solution do
  @spec get_common(nums1 :: [integer], nums2 :: [integer]) :: integer
  def get_common(nums1, nums2) do
    intersection =
      MapSet.intersection(MapSet.new(nums1), MapSet.new(nums2))
      |> MapSet.to_list()

    if intersection != [], do: Enum.min(intersection), else: -1
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test get_common" do
    assert Solution.get_common([1], [2]) == -1
    assert Solution.get_common([1, 2, 3, 6], [2, 3, 4, 5]) == 2
    assert Solution.get_common([1, 2, 3], [2, 4]) == 2

    assert Solution.get_common(
             [11, 15, 28, 31, 36, 42, 46, 54, 58, 63, 64, 67, 75, 76, 76, 79, 83, 85, 87, 90],
             [3, 6, 8, 13, 15, 19, 22, 25, 29, 29, 32, 35, 43, 43, 48, 55, 81, 90, 91, 94]
           ) == 15
  end
end
