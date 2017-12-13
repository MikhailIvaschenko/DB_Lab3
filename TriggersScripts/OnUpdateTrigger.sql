drop trigger if exists `addAnUpdate`;
delimiter //
create trigger `addAnUpdate` before update on `operations`
for each row
begin
if ((select updateTriggerStatus from triggerlog) = "ON") then
update triggerlog
set updateCounter = updateCounter + 1;
end if;
end;