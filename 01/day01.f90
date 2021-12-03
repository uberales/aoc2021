program day01
    use aoc

    implicit none

    integer :: n_lines
    integer, dimension(:), allocatable :: input_data, differences

    integer :: i, v, n_inc

    call count_lines('input.txt', n_lines)

    allocate(input_data(n_lines))

    open(7, file='input.txt')
    do i = 1, n_lines
        read(7, fmt=*) input_data(i)
    enddo
    close(7)

!   part 1

    allocate(differences(n_lines - 1))

    differences = input_data(2:n_lines) - input_data(1:n_lines-1)

    n_inc = 0

    do i = 1,n_lines-1
        if (differences(i) > 0) n_inc = n_inc + 1
    enddo

    write(*,*) n_inc

    deallocate(differences)
    
!   part 2

    allocate(differences(n_lines - 3))
    differences = input_data(4:n_lines) - input_data(1:n_lines-1)

    n_inc = 0

    do i = 1,n_lines-3
        if (differences(i) > 0) n_inc = n_inc + 1
    enddo

    write(*,*) n_inc

!
    deallocate(input_data)

end program

