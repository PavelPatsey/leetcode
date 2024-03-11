defmodule Solution do
  @spec custom_sort_string(order :: String.t(), s :: String.t()) :: String.t()
  def custom_sort_string(order, s) do
    s
    |> String.graphemes()
    |> IO.inspect()
    |> Enum.sort(&get_index(&1, order))
    |> IO.inspect()
  end

  def get_index(char, order) do
    do_get_index(char, String.graphemes(order), 0)
  end

  defp do_get_index(_char, [], _acc) do
    -1
  end

  defp do_get_index(char, [char | _tail], acc) do
    acc
  end

  defp do_get_index(char, [_head | tail], acc) do
    do_get_index(char, tail, acc + 1)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test get_index" do
    assert Solution.get_index("a", "abcd") == 0
    assert Solution.get_index("b", "abcd") == 1
    assert Solution.get_index("d", "abcd") == 3
    assert Solution.get_index("z", "abcd") == -1
  end

  # test "test custom_sort_string" do
  #   assert Solution.custom_sort_string("cba", "abcd") == "dcba"
  # end
end
