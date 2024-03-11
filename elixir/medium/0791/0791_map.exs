defmodule Solution do
  @spec custom_sort_string(order :: String.t(), s :: String.t()) :: String.t()
  def custom_sort_string(order, s) do
    order_map =
      order
      |> String.to_charlist()
      |> Enum.with_index()
      |> Map.new()

    s
    |> String.to_charlist()
    |> Enum.sort_by(&order_map[&1])
    |> List.to_string()
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test custom_sort_string" do
    assert Solution.custom_sort_string("cba", "abcd") == "cbad"
  end
end
