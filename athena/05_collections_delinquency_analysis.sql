--- Collections & Delinquenct Analysis
WITH payments_summary AS (
    SELECT
        payment_status, 
        COUNT(payment_id) AS num_payments, 
        ROUND(AVG(days_past_due), 2) AS avg_dpd
    FROM payments
    GROUP BY payment_status
)
SELECT 
    payment_status, 
    (
        CAST(num_payments AS DECIMAL(10, 2)) / SUM(num_payments) OVER()
    ) * 100 AS relative_frequency, 
    avg_dpd
FROM payments_summary
ORDER BY relative_frequency DESC;

