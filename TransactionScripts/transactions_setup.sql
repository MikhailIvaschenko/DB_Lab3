#set @isolationlvl = 'REPEATABLE READ;';
set @isolationlvl = 'SERIALIZABLE;';

set @localtr = concat('set local transaction isolation level ', @isolationlvl);
set @sessiontr = concat('set session transaction isolation level ', @isolationlvl);
set @globaltr = concat('set global transaction isolation level ', @isolationlvl);

prepare localtr from @localtr;
prepare sessiontr from @sessiontr;
prepare globaltr from @globaltr;

execute localtr;
execute sessiontr;
execute globaltr;

select @@global.transaction_isolation as GlobalIsolation, @@local.transaction_isolation as LocalIsolation, @@session.transaction_isolation as SessionIsolation;