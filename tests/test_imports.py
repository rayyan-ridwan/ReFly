"""Smoke tests for the ReFly package."""

import unittest

from refly import __version__
from refly.agents import BaseAgent
from refly.envs import BaseEnvironment


class PackageImportTests(unittest.TestCase):
    def test_package_exports_version(self) -> None:
        self.assertEqual(__version__, "0.1.0")

    def test_core_interfaces_are_importable(self) -> None:
        self.assertEqual(BaseAgent.__name__, "BaseAgent")
        self.assertEqual(BaseEnvironment.__name__, "BaseEnvironment")


if __name__ == "__main__":
    unittest.main()
