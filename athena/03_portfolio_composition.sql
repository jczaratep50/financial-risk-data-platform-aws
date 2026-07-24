--- Portfolio Composition by Segment
SELECT
    c.segment, 
    COUNT(DISTINCT l.customer_id) AS total_customers, 
    COUNT(l.loan_id) AS total_loans,
    ROUND(SUM(COALESCE(rm.ead)), 2) AS ead,
    ROUND(SUM(COALESCE(rm.expected_loss, 0)), 2) AS expected_loss, 
    ROUND((
        SUM(
            CAST(
                CASE
                    WHEN rm.default_flag = TRUE THEN 1
                    ELSE 0
                END AS DECIMAL(10, 2)
            )
        ) / COUNT(l.loan_id)
    ) * 100, 2) AS default_rate
FROM loans l
LEFT JOIN customers c ON l.customer_id = c.customer_id
LEFT JOIN risk_metrics rm ON l.loan_id = rm.loan_id
GROUP BY segment
ORDER BY expected_loss DESC;

