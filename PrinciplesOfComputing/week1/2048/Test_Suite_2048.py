"""
Test suite for "2048"
"""

import poc_simpletest

def run_suite(test2048):
    """
    Some informal testing code
    """
    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    # test format_function on various inputs (computed, expected, message = "")
    suite.run_test(test2048.reset(), test2048._grid, 'Test #1: test2048.reset()')#NOT SURE ABOUT THIS EXPECTED VALUE
    suite.run_test(test2048.get_grid_height(), test2048._grid_height, 'Test #2: test2048.get_grid_height()')
    suite.run_test(test2048.get_grid_width(), test2048._grid_width, 'Test #3: test2048.get_grid_width()')
    suite.run_test(str(test2048), str('[' + '\n'.join(map(str, test2048._grid)) + ']'),
                   'Test #4: str(test2048)')#NOT SURE ABOUT THIS EXPECTED VALUE
    #suite.run_test(test2048.get_tile(1, 1), 0, 'Test #5: ')




    suite.report_results()
