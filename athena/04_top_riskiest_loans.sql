--- Top Riskiest Loans 
SELECT 
    l.loan_id, 
    l.customer_id,
    p.product_name,
    ROUND(rm.ead, 2),
    ROUND(rm.pd, 2),
    ROUND(rm.lgd, 2),
    ROUND(rm.expected_loss, 2), 
    l.loan_status, 
    rm.risk_rating
FROM loans l
LEFT JOIN products p ON l.product_id = p.product_id
LEFT JOIN risk_metrics rm ON l.loan_id = rm.loan_id
ORDER BY rm.expected_loss DESC
LIMIT 20;
