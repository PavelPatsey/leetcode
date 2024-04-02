defmodule Solution do
  @spec is_isomorphic(s :: String.t(), t :: String.t()) :: boolean
  def is_isomorphic(s, t) do
    [size_s, size_t] =
      [s, t]
      |> Enum.map(&String.to_charlist(&1))
      |> Enum.map(&MapSet.new(&1))
      |> Enum.map(&MapSet.size(&1))

    size_zip =
      [s, t]
      |> Enum.map(&String.to_charlist(&1))
      |> Enum.zip()
      |> MapSet.new()
      |> MapSet.size()

    size_s == size_t and size_t == size_zip
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "is_isomorphic" do
    assert Solution.is_isomorphic("egg", "add") == true
    assert Solution.is_isomorphic("foo", "bar") == false
    assert Solution.is_isomorphic("paper", "title") == true
    assert Solution.is_isomorphic("badc", "baba") == false
  end
end
