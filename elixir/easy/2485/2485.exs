defmodule Solution do
  @spec pivot_integer(n :: integer) :: integer
  def pivot_integer(n) do
    do_pivot_integer(n)
  end

  defp do_pivot_integer(n) do
    total_sum = div(n * (n + 1), 2)
    do_pivot_integer(1, 1, total_sum, n)
  end

  defp do_pivot_integer(i, current_sum, total_sum, n) when i <= n do
    if current_sum == total_sum - current_sum + i do
      i
    else
      do_pivot_integer(i + 1, current_sum + i + 1, total_sum, n)
    end
  end

  defp do_pivot_integer(_, _, _, _), do: -1
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test pivot_integer" do
    assert Solution.pivot_integer(8) == 6
    assert Solution.pivot_integer(1) == 1
    assert Solution.pivot_integer(4) == -1
  end
end
