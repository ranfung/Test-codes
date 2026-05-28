import pandas as pd

data = {
    "Pin": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 26, 28, 29, 30, 31, 32, 34, 35, 36, 37, 40, 41, 42, 43, 44, 46, 47, 48, 49, 50, 52, 53, 54, 55, 56, 58, 59, 66, 67],
    "Signal (Foxconn SDX61)": ["CONFIG_3", "VPH_PWR", "GND", "VPH_PWR", "GND", "FULL_CARD_POWER_OFF#", "USB_D+", "W_DISABLE2#", "USB_D-", "LED_IND_ATC_N", "ANT_TUNER_CONFIG_1", "ANT_TUNER_CONFIG_2", "Reserved", "Reserved", "ANT_TUNER_POWER", "Reserved", "Reserved", "UIM-RESET", "Reserved", "UIM-CLK", "UIM-DATA", "Reserved", "UIM-PWR", "Reserved", "Reserved", "PETp0", "UIM-DATA", "PETn0", "UIM-CLK", "UIM-RESET", "PERp0", "UIM-PWR", "PERn0", "PCIE_RST_N", "PCIE_CLK_REQ_N", "REFCLKp", "PCIE_WAKE_N", "REFCLKn", "MIPI_CLK", "MIPI_DATA", "ANTCTL0", "SIM_DETECT", "RESET#"],
    "Signal (Semtech EM9291)": ["CONFIG_3", "VCC", "GND", "VCC", "GND", "Full_Card_Power_Off_N", "USB_D+", "W_DISABLE_N", "USB_D-", "WWAN_LED_N", "PCIE_DIS", "VBUS_SENSE", "WAKE_ON_WAN_N", "DPR", "GPS_DISABLE_N", "PLA_S2_N", "USB3_TXM", "UIM1_RESET_N", "USB3_TXP", "UIM1_CLK", "UIM1_DATA", "USB3_RXM", "UIM1_PWR", "USB3_RXP", "UIM2_PRES", "PCIE_TXM0", "UIM2_DATA", "PCIE_TXP0", "UIM2_CLK", "UIM2_RESET_N", "PCIE_RXM0", "UIM2_PWR", "PCIE_RXP0", "PCIE_PERST_N", "PCIE_CLKREQ_N", "PCIE_REFCLKM", "PCIE_PEWAKE_N", "PCIE_REFCLKP", "RFFE_CLK", "RFFE_DATA", "ANT_CTRL0", "SIM1_DETECT", "RESET_N"]
}

df = pd.DataFrame(data)
df.to_excel("Pinout_Comparison.xlsx", index=False)
print("File generated successfully.")