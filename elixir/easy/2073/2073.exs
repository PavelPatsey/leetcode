defmodule Solution do
  @spec time_required_to_buy(tickets :: [integer], k :: integer) :: integer
  def time_required_to_buy(tickets, k) do
    k_ticket = Enum.at(tickets, k)
    do_time_required_to_buy(tickets, 0, k, k_ticket, 0)
  end

  defp do_time_required_to_buy([], _i, _k, _k_ticket, acc), do: acc

  defp do_time_required_to_buy([head | tail], i, k, k_ticket, acc) do
    if i <= k do
      do_time_required_to_buy(tail, i + 1, k, k_ticket, acc + min(head, k_ticket))
    else
      do_time_required_to_buy(tail, i + 1, k, k_ticket, acc + min(head, k_ticket - 1))
    end
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test time_required_to_buy" do
    assert Solution.time_required_to_buy([2, 3, 2], 2) == 6
    assert Solution.time_required_to_buy([5, 1, 1, 1], 0) == 8
    assert Solution.time_required_to_buy([84, 49, 5, 24, 70, 77, 87, 8], 3) == 154
  end
end
