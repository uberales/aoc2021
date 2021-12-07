program day06
    use aoc

    implicit none

    integer :: n_elem
    integer, dimension(:), allocatable :: input_data
    
    integer*8 :: fish_count
    
    call count_commas('input.txt', n_elem)
    
    n_elem = n_elem + 1

    allocate(input_data(n_elem))
    
    call load_line('input.txt', n_elem, input_data)
       
    call count_school(n_elem, input_data, 80, fish_count)
    write(*,*) fish_count
    
    call count_school(n_elem, input_data, 256, fish_count)
    write(*,*) fish_count
    
    deallocate(input_data)
    
end program

subroutine count_school(n_elem, school, n_days, fish_count)
    implicit none
    
    integer, intent(in) :: n_elem
    integer, dimension(n_elem), intent(in) :: school
    integer, intent(in) :: n_days
    integer*8, intent(out) :: fish_count
    
    integer*8, dimension(0:8) :: fish_stats
    
    integer :: i
    integer*8 :: f0
    
    fish_stats = 0
    fish_count = 0
    
    do i = 1,n_elem
        fish_stats(school(i)) = fish_stats(school(i)) + 1
    enddo
    
    do i = 1,n_days
        f0 = fish_stats(0)
        fish_stats(0:7) = fish_stats(1:8)
        fish_stats(6) = fish_stats(6) + f0
        fish_stats(8) = f0
    enddo
    
    fish_count = sum(fish_stats)
    
end subroutine
