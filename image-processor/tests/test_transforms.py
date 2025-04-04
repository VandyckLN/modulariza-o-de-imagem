import unittest
from src.transforms.resize import resize
from src.transforms.rotate import rotate

class TestTransforms(unittest.TestCase):

    def test_resize(self):
        # Teste para a função de redimensionamento
        original_image = "path/to/original/image.jpg"
        new_dimensions = (100, 100)
        resized_image = resize(original_image, new_dimensions)
        self.assertEqual(resized_image.size, new_dimensions)

    def test_rotate(self):
        # Teste para a função de rotação
        original_image = "path/to/original/image.jpg"
        angle = 90
        rotated_image = rotate(original_image, angle)
        self.assertEqual(rotated_image.angle, angle)

if __name__ == '__main__':
    unittest.main()