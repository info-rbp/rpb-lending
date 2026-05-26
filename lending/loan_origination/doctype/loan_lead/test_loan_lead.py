# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

import frappe
from frappe.tests import IntegrationTestCase

from lending.loan_management.doctype.loan_application.loan_application import LoanApplication
from lending.loan_origination.doctype.loan_lead.loan_lead import convert_to_loan_application
from lending.tests.test_utils import (
	create_loan_accounts,
	create_loan_product,
	set_loan_settings_in_company,
)


class IntegrationTestLoanLead(IntegrationTestCase):
	def setUp(self):
		set_loan_settings_in_company()
		create_loan_accounts()
		create_loan_product(
			"Home Loan",
			"Home Loan",
			500000,
			9.2,
			0,
			1,
			0,
			repayment_schedule_type="Monthly as per repayment start date",
		)

	def test_convert_to_loan_application_sets_required_defaults(self):
		loan_lead = frappe.get_doc(
			{
				"doctype": "Loan Lead",
				"applicant_type": "Individual",
				"applicant_name": "Casey Borrower",
				"date_of_birth": "1990-01-15",
				"email": "casey.borrower@example.com",
				"loan_product": "Home Loan",
				"loan_amount": 250000,
				"mobile_number": "+91-9102837465",
				"proposed_tenure": 24,
			}
		).insert()

		loan_application_name = convert_to_loan_application(loan_lead.name)
		loan_application = frappe.get_doc("Loan Application", loan_application_name)

		self.assertIsInstance(loan_application, LoanApplication)
		self.assertEqual(loan_application.company, "_Test Company")
		self.assertEqual(loan_application.applicant_type, "Customer")
		self.assertEqual(loan_application.applicant_name, loan_lead.applicant_name)
		self.assertEqual(loan_application.loan_product, loan_lead.loan_product)
		self.assertEqual(loan_application.loan_amount, loan_lead.loan_amount)
		self.assertEqual(loan_application.repayment_periods, loan_lead.proposed_tenure)
		self.assertTrue(loan_application.applicant)

	def test_validate_rejects_future_birth_date(self):
		loan_lead = frappe.get_doc(
			{
				"doctype": "Loan Lead",
				"applicant_type": "Individual",
				"applicant_name": "Future Person",
				"date_of_birth": "2999-01-15",
				"email": "future.person@example.com",
				"loan_product": "Home Loan",
				"loan_amount": 250000,
				"mobile_number": "+91-9102837465",
			}
		)

		self.assertRaises(frappe.ValidationError, loan_lead.insert)