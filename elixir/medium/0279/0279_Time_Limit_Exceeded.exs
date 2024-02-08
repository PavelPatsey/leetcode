defmodule Solution do
  @spec num_squares(n :: integer) :: integer
  def num_squares(n) do
    dp =
      Tuple.duplicate(n, n + 1)
      |> put_elem(0, 0)

    get_num_squares(n, dp, 1, 1)
  end

  def get_num_squares(n, dp, dp_i, sq_i) when dp_i == n and (sq_i + 1) * (sq_i + 1) > n do
    min(elem(dp, dp_i), 1 + elem(dp, dp_i - sq_i * sq_i))
  end

  def get_num_squares(n, dp, dp_i, sq_i) when dp_i - sq_i * sq_i < 0 do
    get_num_squares(n, dp, dp_i + 1, 1)
  end

  def get_num_squares(n, dp, dp_i, sq_i) do
    new_dp = put_elem(dp, dp_i, min(elem(dp, dp_i), 1 + elem(dp, dp_i - sq_i * sq_i)))
    get_num_squares(n, new_dp, dp_i, sq_i + 1)
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
