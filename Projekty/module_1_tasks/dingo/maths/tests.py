from django.test import TestCase
from maths.models import Math, Result

class MathModelTest(TestCase):

    def setUp(self):
        Math.objects.create(operation="add", a=1, b=2)
        Math.objects.create(operation="sub", a=20, b=30)

    def test_math_str(self):
        m1 = Math.objects.get(operation="add")
        m2 = Math.objects.get(operation="sub")

        self.assertEqual(str(m1), "id:1, a=1, b=2, op=add")
        self.assertEqual(str(m2), "id:2, a=20, b=30, op=sub")