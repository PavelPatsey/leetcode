defmodule Solution do
  @spec frequency_sort(s :: String.t()) :: String.t()
  def frequency_sort(s) do
    s
    |> String.graphemes()
    |> Enum.frequencies()
    |> Enum.sort(fn {_, v1}, {_, v2} -> v1 > v2 end)
    |> Enum.map(fn {k, v} -> String.duplicate(k, v) end)
    |> Enum.join("")
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "frequency_sort 1" do
    assert Solution.frequency_sort("tree") == "eetr"
  end

  test "frequency_sort 2" do
    assert Solution.frequency_sort("cccaaa") == "cccaaa"
  end

  test "frequency_sort 3" do
    assert Solution.frequency_sort("bbaA") == "bbaA"
  end
end
