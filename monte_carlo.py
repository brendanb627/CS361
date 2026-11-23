import random
import sys

print("--- OMP Monte Carlo Percentile Calculator (No Dependencies) ---")
print("Enter your values as: optimistic, most_likely, pessimistic")
print("Example: 10, 20, 30")
print("Press Ctrl + C at any time to exit.\n")

# Using 50,000 for pure Python to keep execution instant without NumPy performance overhead
num_simulations = 50000

while True:
  try:
    # Get user input from the terminal
    user_input = input("Enter OMP values: ")

    # Parse and clean the input string into a list of numbers
    cleaned_input = user_input.replace("(", "").replace(")", "")
    parts = [float(x.strip()) for x in cleaned_input.split(",")]

    if len(parts) != 3:
      print("❌ Error: Please enter exactly three numbers separated by commas.")
      continue

    low, mode, high = parts

    # Validate that low <= mode <= high
    if not (low <= mode <= high):
      print(
          "❌ Error: Constraints must follow the rule: Optimistic <= Most"
          " Likely <= Pessimistic"
      )
      continue

    # Run the Monte Carlo simulation using standard Python random module
    samples = [
        random.triangular(low, mode, high) for _ in range(num_simulations)
    ]

    # Sort samples ascending to extract exact percentiles
    samples.sort()

    # Calculate index positions for P50, P80, P90
    p50_idx = int(num_simulations * 0.50)
    p80_idx = int(num_simulations * 0.80)
    p90_idx = int(num_simulations * 0.90)

    p50 = samples[p50_idx]
    p80 = samples[p80_idx]
    p90 = samples[p90_idx]

    # Print results
    print(f"📊 Results:")
    print(f"   P50 (Median) : {p50:.2f}")
    print(f"   P80 (Target) : {p80:.2f}")
    print(f"   P90 (Safe)   : {p90:.2f}")
    print("-" * 40)

  except ValueError:
    print(
        "❌ Error: Invalid number format. Please enter digits separated by"
        " commas."
    )
    print("-" * 40)
  except (KeyboardInterrupt, EOFError):
    print("\n\n👋 Exiting calculator. Goodbye!")
    sys.exit(0)
