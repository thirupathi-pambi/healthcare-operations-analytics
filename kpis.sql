-- Import data/appointments.csv as a table called appointments first.
SELECT clinic, COUNT(*) AS appointments,
 SUM(CASE WHEN status='completed' THEN 1 ELSE 0 END) AS completed,
 ROUND(100.0 * SUM(CASE WHEN status='no_show' THEN 1 ELSE 0 END) / COUNT(*), 1) AS no_show_pct,
 ROUND(100.0 * SUM(CASE WHEN status='cancelled' THEN 1 ELSE 0 END) / COUNT(*), 1) AS cancelled_pct
FROM appointments GROUP BY clinic ORDER BY clinic;
