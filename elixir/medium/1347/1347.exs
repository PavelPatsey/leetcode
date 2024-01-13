defmodule Solution do
  @spec min_steps(s :: String.t(), t :: String.t()) :: integer
  def min_steps(s, t) do
    [s_map, t_map] =
      [s, t]
      |> Enum.map(&String.codepoints/1)
      |> Enum.map(&Enum.frequencies/1)

    Enum.map(s_map, fn {key, value} ->
      if key in Map.keys(t_map) do
        difference = Map.get(s_map, key) - Map.get(t_map, key)

        if difference < 0 do
          0
        else
          difference
        end
      else
        value
      end
    end)
    |> Enum.sum()
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test_1" do
    assert Solution.min_steps("bab", "aba") == 1
  end

  test "test_2" do
    assert Solution.min_steps("leetcode", "practice") == 5
  end

  test "test_3" do
    assert Solution.min_steps("anagram", "mangaar") == 0
  end
end
