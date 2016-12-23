from conans import ConanFile
from conans.tools import download, unzip
import os

class CppUTest(ConanFile):
	name = "CppUTest"
	version = "3.8"
	description = """
		CppUTest is a C /C++ based unit xUnit test framework for unit testing and for test-driving your code. 
		It is written in C++ but is used in C and C++ projects and frequently used in embedded systems but it works for any C/C++ project.
		"""
	url = "https://cpputest.github.io/"
	license = "BSD-3-Clause"
	author = "Mathias Spiessens"
	build_policy = "missing"
	
	def source(self):
		download("https://github.com/cpputest/cpputest/releases/download/v3.8/cpputest-3.8.zip", "cpputest-3.8.zip")
		unzip("cpputest-3.8.zip")
		os.unlink("cpputest-3.8.zip")

	def build(self):
		self.run("cd cpputest-3.8/cpputest_build; autoreconf .. -i; ../configure; make")

	def package(self):
		self.copy("*.h", "include/CppUTest", "cpputest-3.8/include/CppUTest")
		self.copy("*.h", "include/CppUTestExt", "cpputest-3.8/include/CppUTestExt")
		self.copy("*.a", "library", "cpputest-3.8/cpputest_build/lib")
