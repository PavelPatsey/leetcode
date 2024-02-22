defmodule Solution do
  @spec find_judge(n :: integer, trust :: [[integer]]) :: integer
  def find_judge(n, trust) do
    [nodes, children] =
      trust
      |> Enum.map(&List.to_tuple/1)
      |> Enum.unzip()
      |> Tuple.to_list()
      |> Enum.map(&Enum.frequencies/1)

    keys =
      1..n
      |> Enum.to_list()

    do_find_judge(keys, nodes, children, n)
  end

  defp do_find_judge([], _nodes, _children, _n), do: -1

  defp do_find_judge([head | tail], nodes, children, n) do
    if Map.get(nodes, head, 0) == 0 and Map.get(children, head, 0) == n - 1 do
      head
    else
      do_find_judge(tail, nodes, children, n)
    end
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "find_judge" do
    assert Solution.find_judge(2, [[1, 2]]) == 2
    assert Solution.find_judge(3, [[1, 3], [2, 3]]) == 3
    assert Solution.find_judge(2, [[1, 3], [2, 3], [3, 1]]) == -1
    assert Solution.find_judge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]) == 3
  end
end
