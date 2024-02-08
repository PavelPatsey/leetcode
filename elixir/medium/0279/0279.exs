defmodule Solution do
  @spec num_squares(n :: integer) :: integer
  def num_squares(n) do
    get_num_squares(n, %{0 => 0}, 1, 1)
  end

  def get_num_squares(n, dp, key, s) when key == n and (s + 1) * (s + 1) > n do
    min(Map.get(dp, key), 1 + Map.get(dp, key - s ** 2))
  end

  def get_num_squares(n, dp, key, s) when key - s * s < 0 do
    get_num_squares(n, dp, key + 1, 1)
  end

  def get_num_squares(n, dp, key, s) do
    new_dp = Map.put(dp, key, min(Map.get(dp, key), 1 + Map.get(dp, key - s ** 2)))
    get_num_squares(n, new_dp, key, s + 1)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test num_squares 1" do
    assert Solution.num_squares(1) == 1
  end

  test "test num_squares 2" do
    assert Solution.num_squares(2) == 2
  end

  test "test num_squares 3" do
    assert Solution.num_squares(3) == 3
  end

  test "test num_squares 4" do
    assert Solution.num_squares(4) == 1
  end

  test "test num_squares 5" do
    assert Solution.num_squares(5) == 2
  end

  test "test num_squares 7" do
    assert Solution.num_squares(7) == 4
  end

  test "test num_squares 8" do
    assert Solution.num_squares(8) == 2
  end

  test "test num_squares 12" do
    assert Solution.num_squares(12) == 3
  end

  test "test num_squares 13" do
    assert Solution.num_squares(13) == 2
  end
end
