"""
Test suite for format function in "Stopwatch - The game"
"""

import poc_simpletest

def run_suite(twentyfortyeight):
    """
    Some informal testing code
    """
    
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()
    
    # test format_function on various inputs
    suite.run_test(str(twentyfortyeight), "string grid", "Test #1:")
    
    suite.report_results()
    
    



