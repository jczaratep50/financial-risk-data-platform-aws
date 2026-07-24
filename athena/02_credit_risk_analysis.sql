--- Credit Risk Analysis by Product
SELECT 
    p.product_name AS product, 
    COUNT(l.loan_id) AS loans, 
    SUM(rm.ead) AS ead, 
    SUM(rm.expected_loss) AS expected_loss, 
    ROUND(AVG(rm.pd) * 100, 2) AS avg_pd, 
    ROUND(AVG(rm.lgd) * 100, 2) AS avg_lgd
FROM loans l
LEFT JOIN products p ON l.product_id = p.product_id
LEFT JOIN risk_metrics rm ON l.loan_id = rm.loan_id
GROUP BY product_name
ORDER BY expected_loss DESC;
