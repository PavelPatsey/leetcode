defmodule Solution do
  @spec climb_stairs(n :: integer) :: integer
  def climb_stairs(n) do
    _climb_stairs(n, 1, 0, 1)
  end

  defp _climb_stairs(n, n, a, b), do: a + b
  defp _climb_stairs(n, step, a, b), do: _climb_stairs(n, step + 1, b, a + b)
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.climb_stairs(3) == 3
  end

  test "test_2" do
    assert Solution.climb_stairs(4) == 5
  end
end
