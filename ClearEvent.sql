SET GLOBAL event_scheduler = ON;
DROP EVENT IF EXISTS `clearTriggerLog`;
set @newTriggerStatus = "ON";

CREATE EVENT `clearTriggerLog`
ON SCHEDULE EVERY 1 MONTH
DO
call resetProcedure(@newTriggerStatus);


SELECT * FROM `INFORMATION_SCHEMA`.`EVENTS`
WHERE `EVENT_NAME` = 'clearTriggerLog';