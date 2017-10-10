from .. utils import TranspileTestCase, UnaryOperationTestCase, BinaryOperationTestCase, InplaceOperationTestCase


class BytearrayTests(TranspileTestCase):
    def test_setattr(self):
        self.assertCodeExecution("""
            x = bytearray([1,2,3])
            try:
                x.attr = 42
            except AttributeError as err:
                print(err)
            """)

    def test_getattr(self):
        self.assertCodeExecution("""
            x = bytearray([1,2,3])
            try:
                print(x.attr)
            except AttributeError as err:
                print(err)
            """)
    def test_contains(self):
        self.assertCodeExecution("""
            x = bytearray([1,2,3])
            y = bytearray([1,2])
            print(x in y)
            print(y in x)
            """)
        self.assertCodeExecution("""
            print(bytearray([1,2,3]) in bytearray([1,2]))
            print(bytearray([1,2]) in bytearray([1,2,3]))
            print(bytearray([1,2,4]) in bytearray([1,2,3]))
            print(bytearray([8,9,0,1]) in bytearray([1,2,3]))
            print(101 in bytearray([1,2,3]))
            print(101 in bytearray([1,2,3,101]))
            print(b'pybee' in bytearray([1,2]))
            print(bytearray([1,2]) in b'pybee')
        """)
        self.assertCodeExecution("""
            print(300 in bytearray([1,2,3])) #Test ValueError invalid integer range
        """, exits_early=True)
        self.assertCodeExecution("""
            print(['b', 'e'] in bytearray([1,2,3])) #Test TypeError invalid byte array
        """, exits_early=True)


class UnaryBytearrayOperationTests(UnaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]


class BinaryBytearrayOperationTests(BinaryOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]

    not_implemented_versions = {
        'test_modulo_complex': (3.4, ),
    }


class InplaceBytearrayOperationTests(InplaceOperationTestCase, TranspileTestCase):
    data_type = 'bytearray'

    not_implemented = [
    ]

    not_implemented_versions = {
        'test_modulo_complex': (3.4, ),
    }
