defmodule Solution do
  @spec find_matrix(nums :: [integer]) :: [[integer]]
  def find_matrix(nums) do
    counter = Enum.frequencies(nums) |> IO.inspect()
    matrix = Enum.map(counter, fn {k, v} -> List.duplicate(k, v) end) |> IO.inspect()
    Transp.transpose(matrix) |> IO.inspect()
  end
end

defmodule Transp do
  def transpose([]), do: []
  def transpose([[] | xss]), do: transpose(xss)

  def transpose([[x | xs] | xss]) do
    [[x | for([h | _t] <- xss, do: h)] | transpose([xs | for([_h | t] <- xss, do: t)])]
  end
end
