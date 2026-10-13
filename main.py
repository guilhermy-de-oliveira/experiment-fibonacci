################
# DEPENDENCIES #
################

# Library for plotting Cartesian planes.
import matplotlib.pyplot as plt
from matplotlib.patches import Arc

# Standard math library.
import math

##################
# MAIN VARIABLES #
##################

# Number of Fibonacci terms, n.
n_terms: int = 0
# Previous and current numbers.
prev, curr = 0, 1
# List that contains each Fibonacci term.
fib_seq = []

#############
# FUNCTIONS #
#############

# Function that computes the limit-of-ratio operation between consecutive Fibonacci terms.
# The definition states that the larger the term position,
# F(n) / F(n-1) will be closer to the golden ratio constant,
# represented by phi (ϕ) ≈ 1.618...
def generate_golden_ratio_convergence():
    # List that stores the ratios.
    ratios = []
    # List that stores the term positions (important for the X axis of the plot).
    indices = []
    # For each position between 2 and the length of the calculated Fibonacci sequence,
    # add the ratio of the term at index i divided by the previous term,
    # then store each obtained value in the respective lists.
    for i in range(2, len(fib_seq)):
        ratio = fib_seq[i] / fib_seq[i-1]
        ratios.append(ratio)
        indices.append(i)

    # Function return
    return indices, ratios

# Function to plot the convergence graph.
def plot_graph():
    # Get the X and Y values from the function that computes them for us.
    indices, ratios = generate_golden_ratio_convergence()

    # Golden ratio constant, represented by phi (ϕ).
    # The constant itself is not used as a raw repeating decimal since it is an irrational number,
    # defined by: (1 + sqrt(5)) / 2.
    golden_ratio = (1 + math.sqrt(5)) / 2

    # Force the plot to appear in a separate window (important because another plot will also be shown).
    plt.figure()
    # Plot the ratios.
    plt.plot(
        indices,
        ratios,
        marker="o",
        color="blue",
        label="Ratio F(n) / F(n-1)"
    )

    # Create a horizontal line at the exact golden ratio for comparison.
    plt.axhline(
        y=golden_ratio,
        color='red',
        linestyle='--',
        label=f'Exact Golden Ratio ({golden_ratio:.4f})'
    )

    # Define plot properties.
    plt.title('Convergence of the Fibonacci Sequence to the Golden Ratio (Starting from the 3rd Term)')
    plt.xlabel('Term Position (n)')
    plt.ylabel('Ratio Value')
    plt.grid(True)
    plt.legend()

    # Turn on interactive mode and show the plot.
    plt.ion()
    plt.show()

# Function responsible for drawing the golden spiral.
def draw_golden_spiral():
    # Returns the figure and axis for drawing.
    fig, ax = plt.subplots(figsize=(8, 8))
    # Initial position.
    x, y = 0, 0
    # Directions used to place squares/arcs.
    directions = [(0, -1), (-1, -1), (-1, 0), (0, 0)]

    # For each term (side length) in the Fibonacci sequence:
    for i, side in enumerate(fib_seq):
        # The direction for this term is determined by i modulo 4.
        dir_x, dir_y = directions[i % 4]

        # Origin of the current square.
        origin_x = x + dir_x * side
        origin_y = y + dir_y * side

        # Define arc properties depending on direction.
        if i % 4 == 0:
            arc_center = (origin_x, origin_y)
            angle_start, angle_end = 0, 90
            x, y = origin_x + side, origin_y
        elif i % 4 == 1:
            arc_center = (origin_x, origin_y + side)
            angle_start, angle_end = 270, 0
            x, y = origin_x, origin_y
        elif i % 4 == 2:
            arc_center = (origin_x + side, origin_y + side)
            angle_start, angle_end = 180, 270
            x, y = origin_x, origin_y + side
        elif i % 4 == 3:
            arc_center = (origin_x + side, origin_y)
            angle_start, angle_end = 90, 180
            x, y = origin_x + side, origin_y + side

        # Create and add the square patch for this term.
        square = plt.Rectangle((origin_x, origin_y), side, side, edgecolor='gray', facecolor='none', alpha=0.5)
        ax.add_patch(square)

        # Create and add the arc patch for this term.
        arc = Arc(arc_center, side*2, side*2, angle=0, theta1=angle_start, theta2=angle_end, color='gold', linewidth=2)
        ax.add_patch(arc)

    # Finalize plot properties.
    ax.set_aspect('equal', adjustable='box')
    ax.autoscale_view()
    plt.title(f"Golden Spiral with {len(fib_seq)} Fibonacci Squares")
    plt.axis('off')
    # block=True ensures the program waits until the user closes the window.
    plt.show(block=True)

#############
# EXECUTION #
#############

# If this module is the main program, execute the registered events.
if __name__ == "__main__":

    # Console project title
    print(">> FIBONACCI SEQUENCE AND THE GOLDEN RATIO <<")

    # Ask the user how many terms should be calculated.
    # To avoid division by zero and non-natural results, the chosen quantity must be greater than 2 (0, 1, 1)
    # and an integer.
    while n_terms == 0 or n_terms <= 2:
        try:
            n_terms = int(input("Enter the number of terms (n), [n ∈ N, n > 2]: "))
            if (not n_terms > 2):
                print("Please enter a value greater than 2.")
                n_terms = 0
        except ValueError:
            print("Invalid input!")
            n_terms = 0

    # Compute the Fibonacci terms.
    # On each iteration, prev becomes curr and curr becomes prev + curr.
    for _ in range(n_terms):
        fib_seq.append(prev)
        prev, curr = curr, prev + curr

    # Plot the convergence graph and draw the golden spiral.
    plot_graph()
    draw_golden_spiral()
