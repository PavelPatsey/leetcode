defmodule Solution do
  @spec number_of_beams(bank :: [String.t()]) :: integer
  def number_of_beams(bank) do
    bank
    |> Enum.map(&Solution.reduce_row/1)
    |> Enum.filter(fn x -> x > 0 end)
    |> Enum.chunk_every(2, 1, :discard)
    |> Enum.map(&Enum.product/1)
    |> Enum.sum()
  end

  @spec reduce_row(row :: String.t()) :: integer
  def reduce_row(row) do
    row
    |> String.graphemes()
    |> Enum.reduce(0, fn x, acc -> String.to_integer(x) + acc end)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test reduce_row 1" do
    assert Solution.reduce_row("011001") == 3
  end

  test "test reduce_row 2" do
    assert Solution.reduce_row("000000") == 0
  end

  test "test reduce_row 3" do
    assert Solution.reduce_row("010100") == 2
  end

  test "test_1" do
    assert Solution.number_of_beams(["011001", "000000", "010100", "001000"]) == 8
  end

  test "test_2" do
    assert Solution.number_of_beams(["000", "111", "000"]) == 0
  end
end
