defmodule Solution do
  @spec intersection(nums1 :: [integer], nums2 :: [integer]) :: [integer]
  def intersection(nums1, nums2) do
    MapSet.intersection(MapSet.new(nums1), MapSet.new(nums2))
    |> MapSet.to_list()
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test intersection" do
    assert Solution.intersection([1, 2, 2, 1], [2, 2]) == [2]
  end
end
