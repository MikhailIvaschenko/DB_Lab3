drop trigger if exists `addRemoval`;
delimiter //
create trigger `addRemoval` before delete on `operations`
for each row
begin
if ((select deleteTriggerStatus from triggerlog) = "ON") then
update triggerlog
set deleteCounter = deleteCounter + 1;
end if;
end;