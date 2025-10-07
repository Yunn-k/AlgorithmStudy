select count(1) as fish_count
from fish_info m
inner join (
    select fish_name, fish_type
    from fish_name_info
    where 1 = 1
    and fish_name in ('BASS', 'SNAPPER')
    ) x
on m.fish_type = x.fish_type