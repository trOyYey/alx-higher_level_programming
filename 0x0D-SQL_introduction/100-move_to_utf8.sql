-- convert hbtn to UTF8
ALTER DATABASE hbtn_0c_0
MODIFY CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- convert first_table to UTF8
ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER
SET utf8mb4 COLLATE utf8mb4_unicode_ci;
