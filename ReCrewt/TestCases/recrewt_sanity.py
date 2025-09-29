import unittest

from ReCrewt.TestCases.Candidate.test_add_candidate import TestAddCandidate
from ReCrewt.TestCases.Candidate.test_delete_candidate import TestDeleteCandidate
from ReCrewt.TestCases.Employee.test_edit_employee import TestEditEmployee
from ReCrewt.TestCases.Login.test_login import TestLogin
from ReCrewt.TestCases.PostAJob.test_PostAJob import TestPostAJob
from ReCrewt.TestCases.PostAJob.test_job_approved import TestJobApproved
from ReCrewt.TestCases.Report.test_GenerateReport import TestReport

if __name__ == "__main__":
    loader = unittest.TestLoader()
    loader.sortTestMethodsUsing = None

    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestLogin))
    suite.addTests(loader.loadTestsFromTestCase(TestAddCandidate))
    suite.addTests(loader.loadTestsFromTestCase(TestPostAJob))
    suite.addTests(loader.loadTestsFromTestCase(TestJobApproved))
    suite.addTests(loader.loadTestsFromTestCase(TestEditEmployee))
    suite.addTests(loader.loadTestsFromTestCase(TestReport))
    suite.addTests(loader.loadTestsFromTestCase(TestDeleteCandidate))

    runner = unittest.TextTestRunner()
    runner.run(suite)
