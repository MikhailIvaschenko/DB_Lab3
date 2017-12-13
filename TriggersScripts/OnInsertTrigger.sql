drop trigger if exists `addAnInsert`;
delimiter //
create trigger `addAnInsert` before insert on `operations`
for each row
begin
if ((select insertTriggerStatus from triggerlog) = "ON") then
update triggerlog
set addCounter = addCounter + 1;
end if;
end;