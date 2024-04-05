defmodule Solution do
  @spec max_depth(s :: String.t()) :: integer
  def max_depth(s) do
    list =
      s
      |> String.graphemes()

    do_max_depth(list, 0, 0)
  end

  defp do_max_depth([], _current_d, max_d), do: max_d

  defp do_max_depth([head | tail], current_d, max_d) when head == "(" do
    current_d = current_d + 1
    max_d = max(current_d, max_d)
    do_max_depth(tail, current_d, max_d)
  end

  defp do_max_depth([head | tail], current_d, max_d) when head == ")" do
    do_max_depth(tail, current_d - 1, max_d)
  end

  defp do_max_depth([head | tail], current_d, max_d) do
    do_max_depth(tail, current_d, max_d)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "max_depth" do
    assert Solution.max_depth("(1+(2*3)+((8)/4))+1") == 3
    assert Solution.max_depth("(1)+((2))+(((3)))") == 3
  end
end
