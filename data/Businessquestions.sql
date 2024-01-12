-- SELECT FinancialYear, FinancialQuarter, SUM(NumberOfOffences) AS TotalFraudOffenses
-- FROM offenceDetails
-- WHERE ForceName = 'Action Fraud' AND OffenceGroup = 'Fraud offences'
-- GROUP BY FinancialYear, FinancialQuarter
-- ORDER BY FinancialYear, FinancialQuarter;

-- SELECT ForceName, OffenceDescription, SUM(NumberOfOffences) AS TotalViolentOffenses
-- FROM offenceDetails
-- WHERE OffenceSubgroup LIKE 'Violence%' AND ForceName != 'Action Fraud'
-- GROUP BY ForceName, OffenceDescription
-- ORDER BY ForceName, TotalViolentOffenses DESC;

-- SELECT OffenceGroup, OffenceSubgroup, SUM(NumberOfOffences) AS TotalOffences
-- FROM offenceDetails
-- WHERE FinancialYear = '2016/17' AND FinancialQuarter = 1
-- GROUP BY OffenceGroup, OffenceSubgroup
-- ORDER BY TotalOffences DESC;

-- SELECT ForceName, OffenceDescription, SUM(NumberofOffences) AS TotalTheftOffenses
-- FROM offencedetails
-- WHERE OffenceGroup = 'Theft offences'
-- GROUP BY ForceName, OffenceDescription
-- ORDER BY TotalTheftOffenses DESC;

-- SELECT ForceName, 
--        OffenceDescription, 
--        SUM(NumberOfOffences) AS TotalAttemptedBurglaries,
--        SUM(CASE WHEN offenceDescription = 'Solved' THEN NumberOfOffences ELSE 0 END) AS SolvedAttemptedBurglaries,
--        (SUM(CASE WHEN offenceDescription = 'Solved' THEN NumberOfOffences ELSE 0 END) / 
--         SUM(NumberOfOffences)) * 100 AS EnforcementEffectivenessPercentage
-- FROM offencedetails
-- WHERE OffenceSubgroup = 'Non-domestic burglary' AND OffenceDescription = 'Attempted burglary in a building other than a dwelling'
-- GROUP BY ForceName, OffenceDescription
-- ORDER BY EnforcementEffectivenessPercentage DESC;