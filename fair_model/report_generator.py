def generate_report(risk_analysis):
    report_content = f"""
Risk Analysis Report
---------------------
Input Parameters:
- Threat Event Frequency (TEF): {risk_analysis.tef}
- Vulnerability: {risk_analysis.vulnerability}
- Loss Magnitude (Min): {risk_analysis.loss_magnitude_min}
- Loss Magnitude (Max): {risk_analysis.loss_magnitude_max}

Calculated Metrics:
- Loss Event Frequency (LEF): {risk_analysis.calculate_lef()}
- Annual Loss Expectancy (ALE): {risk_analysis.calculate_ale()}
    """

    # Optional: Add recommendations or insights based on the ALE or LEF values.

    report_file = "risk_analysis_report.txt"
    with open(report_file, 'w') as file:
        file.write(report_content)
    
    print(f"Report generated and saved as {report_file}")
