from django.test import TestCase
from django.urls import reverse
from core.models import Legislator, VoteResult, Vote, Bill


class LegislatorDetailViewTest(TestCase):
    def setUp(self):
        self.legislator = Legislator.objects.create(id=1, name="John Doe")
        self.bill = Bill.objects.create(id=1, title="Test Bill", sponsor_id=1)
        self.vote = Vote.objects.create(id=1, bill_id=self.bill.id)
        self.vote_result = VoteResult.objects.create(
            id=1, legislator_id=self.legislator.id, vote_id=self.vote.id, vote_type=1
        )

    def test_legislator_detail_view(self):
        response = self.client.get(
            reverse("legislator_detail", args=[self.legislator.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/legislator_detail.html")

        self.assertEqual(response.context["legislator"], self.legislator)
        self.assertEqual(response.context["bills_supported"], 1)
        self.assertEqual(response.context["bills_opposed"], 0)


class BillDetailViewTest(TestCase):
    def setUp(self):
        self.legislator = Legislator.objects.create(id=1, name="John Doe")
        self.bill = Bill.objects.create(id=1, title="Test Bill", sponsor_id=1)
        self.vote = Vote.objects.create(id=1, bill_id=self.bill.id)
        self.vote_result = VoteResult.objects.create(
            id=1, legislator_id=self.legislator.id, vote_id=self.vote.id, vote_type=2
        )

    def test_bill_detail_view(self):
        response = self.client.get(reverse("bill_detail", args=[self.bill.id]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/bill_detail.html")

        self.assertEqual(response.context["bill"], self.bill)
        self.assertEqual(response.context["votes_in_favor"], 0)
        self.assertEqual(response.context["votes_against"], 1)


class SearchViewTest(TestCase):
    def setUp(self):
        self.legislator = Legislator.objects.create(id=1, name="John Doe")
        self.bill = Bill.objects.create(id=1, title="Test Bill", sponsor_id=1)

    def test_search_view(self):
        response = self.client.get(reverse("search") + "?q=John")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/search_results.html")

        self.assertIn(self.legislator, response.context["legislators"])
        self.assertNotIn(self.bill, response.context["bills"])


class HomeViewTest(TestCase):
    def test_home_view(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")
