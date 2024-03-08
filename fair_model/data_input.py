from risk_analysis import RiskAnalysis

def get_user_input():
    risk_analysis = RiskAnalysis()

    print("Please enter the following risk parameters:")

    tef = float(input("Threat Event Frequency (e.g., 0.5 for twice a year): "))
    vulnerability = float(input("Vulnerability (0 to 1 scale): "))
    loss_magnitude_min = float(input("Minimum Loss Magnitude: "))
    loss_magnitude_max = float(input("Maximum Loss Magnitude: "))

    risk_analysis.set_tef(tef)
    risk_analysis.set_vulnerability(vulnerability)
    risk_analysis.set_loss_magnitude(loss_magnitude_min, loss_magnitude_max)

    return risk_analysis
