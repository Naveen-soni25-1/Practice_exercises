from random import choice

class RandomWalk:
    """A class to generate random walk"""

    def __init__(self, num_points=5_000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # All walks starts at (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def get_step(self):
        """A method to calcuate steps"""
        direction = choice([1, -1])
        distance = choice([0, 1, 3, 4, 5, 6, 7, 8])
        return direction * distance 

    def fill_walk(self):
        """Calculate all the points in the walk"""

        # keep taking steps untill the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            # decide which direction to go, and how far to go.
            x_step = self.get_step()
            y_step = self.get_step()

            # reject moves that go nowhere
            if x_step ==0 and y_step == 0:
                continue

            # Calculate the new_position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)