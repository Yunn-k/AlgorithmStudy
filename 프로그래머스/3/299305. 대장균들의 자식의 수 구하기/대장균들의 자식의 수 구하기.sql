select m.id as id
    , count(x.id) as child_count
from ecoli_data m
left join ecoli_data x 
 on (m.id = x.parent_id)
 group by m.id
 order by id asc 