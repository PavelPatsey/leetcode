defmodule Solution do
  @spec make_equal(words :: [String.t()]) :: boolean
  def make_equal(words) do
    counter =
      Enum.map(words, &String.to_charlist/1)
      |> Enum.concat()
      |> Enum.frequencies()

    Enum.map(counter, fn {_, v} -> rem(v, length(words)) != 0 end)
    |> Enum.any?()
    |> Kernel.!()
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.make_equal(["abc", "aabc", "bc"]) == true
  end

  test "test_2" do
    assert Solution.make_equal(["ab", "a"]) == false
  end
end
