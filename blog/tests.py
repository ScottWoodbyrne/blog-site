from django.test import TestCase
from views import post_list, post_detail
from django.core.urlresolvers import resolve
from accounts.forms import UserRegistrationForm


class SimpleTestCase(TestCase):

    def test_adding_something_simple(self):
        self.assertEqual(1+2, 3)

    def test_adding_something_isnt_equal(self):
        self.assertNotEqual(1 + 2, 4)

    def test_home_page_resolves(self):
        home_page = resolve('/')
        self.assertEqual(home_page.func, post_list)

    def test_home_page_code(self):
        home_page_code = self.client.get('/')
        self.assertEqual(home_page_code.status_code, 200)

    def test_blog_page_resolves(self):
        details_page = resolve('/blog/2/')
        self.assertEqual(details_page.func, post_detail)

    def test_check_template_for_home_is_correct(self):
        blog = self.client.get('/')
        self.assertTemplateUsed(blog, 'blogposts.html')

    def test_registrations_form(self):
        form = UserRegistrationForm({
            'email': 'person@test.com',
            'password1': 'letmein1',
            'password2': 'letmein1',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '9',
            'expiry_year': '2018',
            'stripe_id': 'cus_8wcF8FItG9Z3Nj'
        })

        self.assertTrue(form.is_valid())

    def test_registrations_form_passwords_dont_match(self):
        form = UserRegistrationForm({
            'email': 'person@test.com',
            'password1': 'notthesame',
            'password2': 'letmein1',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '9',
            'expiry_year': '2018',
            'stripe_id': 'cus_8wcF8FItG9Z3Nj'
        })

        self.assertFalse(form.is_valid())


    def test_registrations_form_blank_passwords(self):
        form = UserRegistrationForm({
            'email': 'person@test.com',
            'password1': '',
            'password2': '',
            'credit_card_number': '4242424242424242',
            'cvv': '123',
            'expiry_month': '9',
            'expiry_year': '2018',
            'stripe_id': 'cus_8wcF8FItG9Z3Nj'
        })

        self.assertFalse(form.is_valid())

