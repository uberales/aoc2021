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
    
    subroutine count_commas(file_name, n_commas)
        implicit none
        
        character(len=*), intent(in) :: file_name
        integer, intent(out) :: n_commas
        
        integer :: io, i
        character(len=4096) :: line

        open(7, file=trim(file_name))
        read(7, "(A)") line
        close(7)
                
        line = trim(line)
        n_commas = 0
        
        do i=1,len(trim(line))
            if (line(i:i).eq.',') then
                n_commas = n_commas + 1
            endif
        enddo        
    end subroutine

    subroutine load_line(file_name, n_elem, int_array)
        implicit none
        
        character(len=*), intent(in) :: file_name
        integer, intent(in) :: n_elem        
        integer, dimension(n_elem), intent(out) :: int_array
        
        character(len=4096) :: tmp, line
        
        integer :: i, j, k
        
        tmp(1:4096) = ' '
        int_array = 0
        
        open(7, file=trim(file_name))
        read(7, "(A)") line
        close(7)
                
        j = 0
        k = 1
        do i = 1,4096            
            if (line(i:i).eq.','.and.j.gt.0) then
                read(tmp(1:j), *) int_array(k)
                k = k + 1
                j = 0
            else            
                j = j + 1
                tmp(j:j) = line(i:i)                
            endif     
        enddo
        
        if (j.gt.0) then
            read(tmp(1:j), *) int_array(k)
        endif
        
        
    end subroutine
    
end module
