defmodule Solution do
  @spec count_students(students :: [integer], sandwiches :: [integer]) :: integer
  def count_students(students, sandwiches) do
    do_count_students(students, sandwiches)
    |> length()
  end

  defp do_count_students([], _) do
    []
  end

  defp do_count_students([st_head | st_tail], [sand_head | sand_tail])
       when st_head == sand_head do
    do_count_students(st_tail, sand_tail)
  end

  defp do_count_students(students, sandwiches) do
    [st_head | st_tail] = students
    [sand_head | _sand_tail] = sandwiches

    if sand_head not in students do
      students
    else
      do_count_students(Enum.concat(st_tail, [st_head]), sandwiches)
    end
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test count_students" do
    assert Solution.count_students([1], [1]) == 0
    assert Solution.count_students([1], [0]) == 1
    # assert Solution.count_students([1, 1, 0, 0], [0, 1, 0, 1]) == 0
    # assert Solution.count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3
  end
end
