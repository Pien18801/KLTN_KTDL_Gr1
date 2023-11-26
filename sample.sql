USE myCompany;


INSERT INTO Inventory(quantity) VALUES (221);
INSERT INTO Inventory(quantity) VALUES (348);
INSERT INTO Inventory(quantity) VALUES (64);
INSERT INTO Inventory(quantity) VALUES (175);
INSERT INTO Inventory(quantity) VALUES (375);

INSERT INTO Products(Year,Make,Model,Category,inventory_id,created_at) VALUES (2021,'Plymouth','Prowler','Convertible',2001,'2008-02-28');
INSERT INTO Products(Year,Make,Model,Category,inventory_id,created_at) VALUES (2019,'Oldsmobile','Intrigue','Sedan',2002,'2023-07-26');
INSERT INTO Products(Year,Make,Model,Category,inventory_id,created_at) VALUES (2016,'Hyundai','Sonata Plug-in Hybrid','Sedan',2003,'2022-09-14');
INSERT INTO Products(Year,Make,Model,Category,inventory_id,created_at) VALUES (2017,'Hyundai','Entourage','Van/Minivan',2004,'2001-08-27');
INSERT INTO Products(Year,Make,Model,Category,inventory_id,created_at) VALUES (2020,'Audi','S5','Coupe, Convertible',2005,'2022-07-04');


INSERT INTO Users(username,firstname,lastname,email) VALUES ('ogonzalez','Helen','Black','osbornedebra@example.org');
INSERT INTO Users(username,firstname,lastname,email) VALUES ('vmorgan','Hannah','Peck','eric67@example.net');
INSERT INTO Users(username,firstname,lastname,email) VALUES ('theresaodom','Evan','Wang','sophiataylor@example.com');
INSERT INTO Users(username,firstname,lastname,email) VALUES ('mckenziesteven','Austin','Reed','amy59@example.com');
INSERT INTO Users(username,firstname,lastname,email) VALUES ('martineztim','Brian','Banks','williamdavis@example.org');

INSERT INTO User_detail(user_id,address,city,postcode,country) VALUES (1001,'12749 John Forest
Dawnhaven, MI 94128','West Bradley',17608,'United States Minor Outlying Islands');
INSERT INTO User_detail(user_id,address,city,postcode,country) VALUES (1002,'6385 Chandler Squares Apt. 105
Rebeccafort, MS 04995','North Sarah',58643,'Lithuania');
INSERT INTO User_detail(user_id,address,city,postcode,country) VALUES (1003,'748 Osborne Underpass Apt. 459
Port Janet, NV 57158','Reyesberg',36130,'Palau');
INSERT INTO User_detail(user_id,address,city,postcode,country) VALUES (1004,'69168 Ortega Circles Apt. 398
Charlesville, KS 34750','Lawrenceview',14652,'Wallis and Futuna');
INSERT INTO User_detail(user_id,address,city,postcode,country) VALUES (1005,'7460 Hicks Harbors
Greenton, WY 07163','Cameronville',59824,'South Georgia and the South Sandwich Islands');


INSERT INTO Orders(product_id,quantity,created_at) VALUES (1057,1,'2012-10-20');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (1600,1,'2016-03-29');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (424,1,'2022-02-13');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (424,2,'2012-01-18');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (1622,2,'2013-05-13');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (1622,1,'2003-10-23');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (821,2,'2016-03-29');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (501,1,'2022-02-13');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (501,2,'2012-01-18');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (2001,2,'2013-05-13');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (2003,2,'2003-10-23');
INSERT INTO Orders(product_id,quantity,created_at) VALUES (2003,1,'2012-10-20');


INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10001,148,302046,'instalment');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10002,24,455229,'cash');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10003,18,969499,'instalment');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10004,851,925299,'credit_card');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10005,224,815046,'credit_card');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10006,284,223604,'credit_card');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10007,444,302046,'instalment');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10008,421,725229,'cash');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10009,28,669499,'instalment');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10010,1003,925299,'credit_card');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10011,1001,815046,'credit_card');
INSERT INTO Order_detail(order_id,user_id,total,payment) VALUES (10012,1002,223604,'credit_card');
