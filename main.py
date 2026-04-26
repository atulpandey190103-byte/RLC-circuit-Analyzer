from rlc import RLC

def main():
    try:
        R = float(input("Enter Resistance (Ohm): "))
        L = float(input("Enter Inductance (H): "))
        C = float(input("Enter Capacitance (F): "))
        f = float(input("Enter Frequency (Hz): "))

        circuit = RLC(R, L, C, f)

        print("\n--- Results ---")
        print(f"Inductive Reactance (XL): {circuit.reactance_L():.2f} Ohm")
        print(f"Capacitive Reactance (XC): {circuit.reactance_C():.2f} Ohm")
        print(f"Impedance (Z): {circuit.impedance():.2f} Ohm")
        print(f"Phase Angle (radians): {circuit.phase_angle():.4f}")
        print(f"Resonant Frequency (Hz): {circuit.resonant_frequency():.2f}")

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
