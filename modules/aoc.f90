module aoc
    implicit none

    contains

    subroutine count_lines(file_name, n_lines)
        implicit none

        character(len=*), intent(in) :: file_name
        integer, intent(out) :: n_lines

        integer :: io

        open(7, file=trim(file_name))

        n_lines = 0
        do
            read(7, *, iostat=io)
            if (io.ne.0) exit
            n_lines = n_lines + 1
        enddo

        close(7)

    end subroutine

end module