defmodule Solution do
  @spec find_winners(matches :: [[integer]]) :: [[integer]]
  def find_winners(matches) do
    players =
      List.flatten(matches)
      |> MapSet.new()

    losers_frequencies =
      matches
      |> Enum.map(fn [_, x] -> x end)
      |> Enum.frequencies()

    [0, 1]
    |> Enum.map(fn x -> losers_filter(players, losers_frequencies, x) end)
  end

  @spec losers_filter(players :: [integer], frequencies :: Map, n :: integer) :: [[integer]]
  def losers_filter(players, frequencies, n) do
    players
    |> Enum.filter(fn player ->
      if Map.get(frequencies, player, 0) == n, do: true, else: false
    end)
    |> Enum.sort()
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test losers_filter 1" do
    assert Solution.losers_filter([1, 2, 3], %{1 => 1, 2 => 2, 3 => 3}, 1) == [1]
  end

  test "test losers_filter 2" do
    assert Solution.losers_filter([1, 2, 3], %{1 => 0, 2 => 0, 3 => 3}, 0) == [1, 2]
  end

  test "test_1" do
    assert Solution.find_winners([
             [1, 3],
             [2, 3],
             [3, 6],
             [5, 6],
             [5, 7],
             [4, 5],
             [4, 8],
             [4, 9],
             [10, 4],
             [10, 9]
           ]) == [[1, 2, 10], [4, 5, 7, 8]]
  end

  test "test_2" do
    assert Solution.find_winners([[2, 3], [1, 3], [5, 4], [6, 4]]) == [[1, 2, 5, 6], []]
  end
end
