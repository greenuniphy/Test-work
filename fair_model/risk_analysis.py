class RiskAnalysis:
    def __init__(self):
        self.tef = None  # Threat Event Frequency
        self.vulnerability = None
        self.loss_magnitude_min = None
        self.loss_magnitude_max = None

    def set_tef(self, tef):
        self.tef = tef

    def set_vulnerability(self, vulnerability):
        self.vulnerability = vulnerability

    def set_loss_magnitude(self, min_value, max_value):
        self.loss_magnitude_min = min_value
        self.loss_magnitude_max = max_value

    def calculate_lef(self):
        # Loss Event Frequency = TEF * Vulnerability
        return self.tef * self.vulnerability

    def calculate_ale(self):
        # Annual Loss Expectancy = LEF * Average Loss Magnitude
        average_loss_magnitude = (self.loss_magnitude_min + self.loss_magnitude_max) / 2
        return self.calculate_lef() * average_loss_magnitude
