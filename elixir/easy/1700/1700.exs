defmodule Solution do
  @spec count_students(students :: [integer], sandwiches :: [integer]) :: integer
  def count_students(students, sandwiches) do
    do_count_students(students, sandwiches)
  end

  defp do_count_students([], []), do: 0

  defp do_count_students([students_head | students_tail], [sandwiches_head | sandwiches_tail])
       when students_head == sandwiches_head do
    do_count_students(students_tail, sandwiches_tail)
  end

  defp do_count_students(students, sandwiches) do
    [students_head | students_tail] = students

    if hd(sandwiches) not in students do
      length(students)
    else
      do_count_students(Enum.concat(students_tail, [students_head]), sandwiches)
    end
  end
end

ExUnit.start()

defmodule AssertionTest do
  use ExUnit.Case, async: true

  test "test count_students" do
    assert Solution.count_students([1], [1]) == 0
    assert Solution.count_students([1], [0]) == 1
    assert Solution.count_students([1, 1, 0, 0], [0, 1, 0, 1]) == 0
    assert Solution.count_students([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3
  end
end
