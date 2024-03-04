defmodule Solution do
  @spec bag_of_tokens_score(tokens :: [integer], power :: integer) :: integer
  def bag_of_tokens_score(tokens, power) do
    tokens_tuple =
      tokens
      |> Enum.sort()
      |> List.to_tuple()

    do_score(tokens_tuple, power, 0, 0, tuple_size(tokens_tuple) - 1)
  end

  defp do_score(tokens, power, score, l, r)
       when l <= r and elem(tokens, l) <= power do
    do_score(tokens, power - elem(tokens, l), score + 1, l + 1, r)
  end

  defp do_score(tokens, power, score, l, r)
       when l < r and score >= 1 do
    do_score(tokens, power + elem(tokens, r), score - 1, l, r - 1)
  end

  defp do_score(_tokens, _power, score, _l, _r), do: score
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test bag_of_tokens_score" do
    assert Solution.bag_of_tokens_score([100], 50) == 0
    assert Solution.bag_of_tokens_score([200, 100], 150) == 1
    assert Solution.bag_of_tokens_score([100, 200, 300, 400], 200) == 2
  end
end
