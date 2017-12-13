#1. Lost update => durring a simultaneous changing of a table by  
#				   different transactions an update might be lost 
#R-R: on repeatable read current transaction's updates are stopped
#	  before the previous transaction's updates are commited
#SL: --||--
start transaction; #1
update accounts set acPrice = acPrice + 100 where currency = 'dollar'; #2
commit; #5

#2. Dirty reading => data manipulations by a transaction  
#				  that is not gonna be commited 
#R-R: on repeatable read the second transaction gets the data
#	  that the table had had before the first transaction was executed
#SL: --||--
start transaction; #1
update accounts set acPrice = acPrice + 100 where acCurrency = 'dollar'; #2
rollback; # 5

#3. Nonrepeated reading => when durring a double reading the same data in second transaction
#						the first-read data is changed before the second read by 1st transaction
#R-R: gets the data from the first selection even though the second selection has been commited
#SL: --||--
start transaction; #3
update accounts set acPrice = acPrice + 100 where acCurrency = 'dollar'; #4
commit; #5

#4. Phantom reading => when durring a double reading in terms of the same transaction
#					   same selects give different results
#R-R: returns the first-read selection => phantom read does not happen
#SL: --||--
start transaction; #3
insert into accounts (acID, acDate, acOperation_type, acPrice, acCurrency, acGoods_type)
VALUES ('account5', '2017-10-10', 'type4', 1112, 'dollar', 'goodstype'); #4
commit; #5