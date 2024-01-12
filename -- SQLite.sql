-- SQLite
--     CREATE TABLE sleep (
--       date INTEGER,
--       snooze INTEGER,
--       efficiency INTEGER,
--     score INTEGER
--   );

 .mode csv
  .import '/Users/aruha/DSprograming2/DSprograming2/sleep1.csv' sleep
 SELECT * FROM sleep;