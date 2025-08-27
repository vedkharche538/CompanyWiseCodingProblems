SELECT 
    userid, 
    SUM(balance_change) AS balance
FROM (
    SELECT senderid AS userid, -amount AS balance_change 
    FROM transactions
    UNION ALL
    SELECT receiverid AS userid, amount AS balance_change 
    FROM transactions
) AS t
GROUP BY userid
ORDER BY userid;