import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import support_data

class SupportDataTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db = Path(self.temp_dir.name) / "test.db"
        self.patch = patch.object(support_data, "DB_PATH", self.db)
        self.patch.start()
        support_data.initialize_database()

    def tearDown(self):
        self.patch.stop()
        self.temp_dir.cleanup()

    def test_known_service_returns_synthetic_source(self):
        result = support_data.check_service_status("VPN")
        self.assertTrue(result["success"])
        self.assertEqual(result["data_source"], "synthetic_local_demo_data")

    def test_unknown_service_is_rejected(self):
        result = support_data.check_service_status("Payroll")
        self.assertFalse(result["success"])

    def test_create_and_retrieve_ticket(self):
        created = support_data.create_support_ticket(
            "Wi-Fi unavailable",
            "Several demo laptops cannot access the internet.",
            "Wi-Fi",
            "High",
            "Wi-Fi",
            "Demo office",
        )
        self.assertTrue(created["success"])
        ticket_id = created["ticket"]["ticket_id"]
        retrieved = support_data.get_ticket_status(ticket_id)
        self.assertTrue(retrieved["success"])
        self.assertEqual(retrieved["ticket"]["status"], "Open")

    def test_invalid_priority_is_rejected(self):
        result = support_data.create_support_ticket(
            "Test issue", "Test description", "Network", "Urgent",
            "Internet", "Demo office"
        )
        self.assertFalse(result["success"])

    def test_password_like_content_is_rejected(self):
        result = support_data.create_support_ticket(
            "Login issue", "password: Secret123", "Application", "Low",
            "Business Application", "Demo office"
        )
        self.assertFalse(result["success"])

if __name__ == "__main__":
    unittest.main()
