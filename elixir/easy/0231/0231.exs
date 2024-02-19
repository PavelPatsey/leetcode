defmodule Solution do
  @spec is_power_of_two(n :: integer) :: boolean
  def is_power_of_two(n) do
    do_is_power_of_two(n, 1)
  end

  @spec do_is_power_of_two(n :: integer, acc :: integer) :: boolean
  defp do_is_power_of_two(n, _acc) when n <= 0 do
    false
  end

  defp do_is_power_of_two(n, acc) when acc == n do
    true
  end

  defp do_is_power_of_two(n, acc) when acc > n do
    false
  end

  defp do_is_power_of_two(n, acc) do
    do_is_power_of_two(n, acc * 2)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test is_power_of_two" do
    assert Solution.is_power_of_two(-4) == false
    assert Solution.is_power_of_two(-3) == false
    assert Solution.is_power_of_two(0) == false
    assert Solution.is_power_of_two(1) == true
    assert Solution.is_power_of_two(2) == true
    assert Solution.is_power_of_two(16) == true
    assert Solution.is_power_of_two(3) == false
  end
end
