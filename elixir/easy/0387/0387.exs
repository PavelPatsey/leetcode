defmodule Solution do
  @spec first_uniq_char(s :: String.t()) :: integer
  def first_uniq_char(s) do
    graphemes = String.graphemes(s)

    frequencies =
      graphemes
      |> Enum.frequencies()

    enumerated = Enum.with_index(graphemes)

    Enum.find(enumerated, {nil, -1}, fn {char, _} -> Map.get(frequencies, char) == 1 end)
    |> elem(1)
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.first_uniq_char("leetcode") == 0
  end

  test "test_2" do
    assert Solution.first_uniq_char("loveleetcode") == 2
  end

  test "test_3" do
    assert Solution.first_uniq_char("aabb") == -1
  end
end
