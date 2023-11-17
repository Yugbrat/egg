import unittest

class TestEggCatcherGame(unittest.TestCase):

    def test_egg_movement(self):
        # Test if eggs move down after calling move_eggs
        # The test checks if the y-coordinates of eggs increase after calling move_eggs
        initial_y_positions = [c.coords(egg)[1] for egg in eggs]
        move_eggs()
        updated_y_positions = [c.coords(egg)[1] for egg in eggs]
        self.assertGreater(min(updated_y_positions), min(initial_y_positions))

    def test_lose_a_life(self):
        # Test if lives decrease after calling lose_a_life
        # The test simulates losing a life and checks if the number of lives decreases by 1
        initial_lives = lives_remaining
        lose_a_life()
        self.assertEqual(lives_remaining, initial_lives - 1)

    def test_egg_dropped_game_over(self):
        # Test if the game ends when there are no remaining lives after an egg is dropped
        # The test simulates dropping an egg and losing all lives, then checks if the game over message is displayed
        global lives_remaining, score
        lives_remaining = 1  # Set initial lives to 1 for the test
        egg_to_drop = c.create_oval(50, canvas_height, 95, canvas_height + egg_height, fill='red', width=0)
        eggs.append(egg_to_drop)
        egg_dropped(egg_to_drop)
        self.assertEqual(lives_remaining, 0)  # Ensure lives are reduced to 0
        with self.assertRaises(SystemExit):
            root.destroy()  # Check if the root is destroyed, indicating the game over

    def test_increase_score_speed_interval(self):
        # Test if score increases and egg speed and interval decrease after catching an egg
        # The test simulates catching an egg and checks if the score increases, and egg speed and interval decrease
        initial_score = score
        initial_speed = egg_speed
        initial_interval = egg_interval
        egg_to_catch = c.create_oval(50, 50, 95, 95, fill='red', width=0)  # Create a mock egg
        eggs.append(egg_to_catch)
        check_catch()
        self.assertGreater(score, initial_score)
        self.assertLess(egg_speed, initial_speed)
        self.assertLess(egg_interval, initial_interval)

    def test_catcher_movement(self):
        # Test if the catcher moves left and right correctly
        # The test simulates pressing the left and right arrow keys and checks if the catcher's x-coordinates change accordingly
        initial_x1, _, _, _ = c.coords(catcher)
        move_left(None)
        new_x1, _, _, _ = c.coords(catcher)
        self.assertLess(new_x1, initial_x1)  # Check if the x-coordinate decreases after moving left

        initial_x2, _, _, _ = c.coords(catcher)
        move_right(None)
        new_x2, _, _, _ = c.coords(catcher)
        self.assertGreater(new_x2, initial_x2)  # Check if the x-coordinate increases after moving right

if __name__ == '__main__':
    unittest.main()
