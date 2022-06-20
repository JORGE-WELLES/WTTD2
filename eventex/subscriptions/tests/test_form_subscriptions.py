from unittest import TestCase

from eventex.subscriptions.forms import SubscriptionForm


class SubscripitionFormTest(TestCase):
    def setUp(self):
        self.form = SubscriptionForm()

    def test_has_form_fields(self):
        """ Form must have 4 fields """
        expected = ['name', 'cpf', 'email', 'telefone']
        self.assertSequenceEqual(expected, list(self.form.fields))
