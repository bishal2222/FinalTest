with ranks as (select  distinct salary, d.name as department, e.name as Employee, dense_rank() over(partition by d.name order by salary desc) as ranks
from employee e
left join department d
on e.departmentId = d.id
group by salary, department, Employee
order by salary desc)
select department, employee, salary
from ranks
where ranks <= 3  