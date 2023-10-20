import unittest
import os
from readme_thumbnails import WALLPAPERS_DIR, THUMBNAILS_DIR, README_FILE

class TestThumbnailGeneration(unittest.TestCase):

    def test_directories(self):
        """Test if directories are set up correctly."""
        self.assertTrue(os.path.exists(WALLPAPERS_DIR))
        self.assertTrue(os.path.exists(THUMBNAILS_DIR))

    def test_readme_exists(self):
        """Test if README file exists after running the script."""
        self.assertTrue(os.path.exists(README_FILE))
        
    # Add more tests as needed...

if __name__ == "__main__":
    unittest.main()

