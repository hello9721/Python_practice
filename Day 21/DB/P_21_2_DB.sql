CREATE TABLE "UserData" (
	"CODE" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"NAME" TEXT NOT NULL,
	"BUY" TEXT
	)
	
ALTER TABLE UserData add "PAID" INTEGER;
ALTER TABLE UserData add "ADDRESS" TEXT;

ALTER TABLE UserData DROP "ADDRESS";

INSERT INTO UserData(NAME, PAID) VALUES ("K", 503300);
INSERT INTO UserData(NAME, BUY, PAID) VALUES ("A", "NS", 353300);
INSERT INTO UserData(NAME, PAID) VALUES ("B", 1500000);
INSERT INTO UserData(NAME, PAID) VALUES ("C", 703000);
INSERT INTO UserData(NAME, PAID) VALUES ("D", 900000);
INSERT INTO UserData(NAME, BUY) VALUES ("N", "LP Player");

UPDATE UserData SET BUY = "Laptop" WHERE name = "K";
UPDATE UserData SET CODE = 2 WHERE name = "N";
UPDATE UserData SET BUY = "iPhone14" WHERE name = "B";
UPDATE UserData SET BUY = "MicroWave" WHERE name = "C";
UPDATE UserData SET BUY = "SmartTV" WHERE name = "D";
UPDATE UserData SET PAID = 370000 WHERE BUY = "LP Player";

DELETE FROM UserData WHERE ROWID = 2;

SELECT * FROM UserData ORDER by PAID DESC;

INSERT INTO ProData(ProductName, Price) VALUES ("Laptop", 500000);
INSERT INTO ProData(ProductName, Price) VALUES ("NS", 350000);
INSERT INTO ProData(ProductName, Price) VALUES ("iPhone14", 1500000);
INSERT INTO ProData(ProductName, Price) VALUES ("MicroWave", 700000);
INSERT INTO ProData(ProductName, Price) VALUES ("LP Player", 370000);
INSERT INTO ProData(ProductName, Price) VALUES ("SmartTV", 900000);

SELECT * FROM UserData JOIN ProData;
SELECT CODE, name, ProData.ProductName, PAID FROM UserData JOIN ProData on ProData.ProductName = UserData.BUY;

INSERT INTO ProData(ProductName, Price) VALUES ("ABC", 370000);
INSERT INTO ProData(ProductName, Price) VALUES ("BCDE", 900000);

DELETE FROM ProData WHERE ProductName like "%B%";