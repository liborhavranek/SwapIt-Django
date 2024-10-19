"""
Author: Made with love by Libor Raven
Date: 19.10.2024
"""
from django.test import TestCase
from django.urls import reverse
from ..models import Category


class CategoryListViewTests(TestCase):
    """
    Testování kategorií
    """
    def setUp(self) -> None:
        """
        Přednastaví kategorie pro testování. Vytvoří několik hlavních kategorií,
        podkategorií a nastaví jejich viditelnost.
        """
        self.categories = {
            'electronics': Category.objects.create(name='Elektronika',
                                                   position=1,
                                                   is_visible=True),
            'cars': Category.objects.create(name='Auta',
                                            position=2,
                                            is_visible=True),
            'hidden_category': Category.objects.create(name='Tajná kategorie',
                                                       position=3,
                                                       is_visible=False)
        }

        self.subcategories = {
            'mobiles': Category.objects.create(name='Mobily',
                                               parent=self.categories['electronics'],
                                               position=1,
                                               is_visible=True),
            'laptops': Category.objects.create(name='Notebooky',
                                               parent=self.categories['electronics'],
                                               position=2,
                                               is_visible=True),
            'hidden_subcategory': Category.objects.create(name='Tajná podkategorie',
                                                          parent=self.categories['electronics'],
                                                          position=3,
                                                          is_visible=False)
        }

        self.sub_subcategories = {
            'smartphones': Category.objects.create(name='Chytré telefony',
                                                   parent=self.subcategories['mobiles'],
                                                   position=1,
                                                   is_visible=True),
            'basic_phones': Category.objects.create(name='Tlačítkové telefony',
                                                    parent=self.subcategories['mobiles'],
                                                    position=2,
                                                    is_visible=True),
            'hidden_sub_subcategory': Category.objects.create(name='Tajná pod-podkategorie',
                                                              parent=self.subcategories['mobiles'],
                                                              position=3,
                                                              is_visible=False)
        }

    def test_view_url_exists_at_proper_location(self) -> None:
        """
        Testuje, zda URL existuje a odpovídá správným view.
        """
        response = self.client.get('/categories/')
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self) -> None:
        """
        Testuje, zda view používá správnou šablonu.
        """
        response = self.client.get(reverse('category_list'))
        self.assertTemplateUsed(response, 'categories.html')

    def test_context_contains_visible_categories(self) -> None:
        """
        Testuje, zda context obsahuje pouze viditelné hlavní kategorie.
        """
        response = self.client.get(reverse('category_list'))
        categories = response.context['categories']
        self.assertIn(self.categories['electronics'], categories)

    def test_context_not_contains_unvisible_categories(self) -> None:
        """
        Testuje, zda context obsahuje pouze viditelné hlavní kategorie.
        """
        response = self.client.get(reverse('category_list'))
        categories = response.context['categories']
        self.assertNotIn(self.categories['hidden_category'], categories)

    def test_context_contains_visible_mobiles(self) -> None:
        """
        Testuje, zda context obsahuje viditelnou podkategorii Mobily v Elektronice.
        """
        self.client.get(reverse('category_list'))
        subcategories = self.categories['electronics'].get_subcategories()
        self.assertIn(self.subcategories['mobiles'], subcategories)

    def test_context_contains_visible_laptops(self) -> None:
        """
        Testuje, zda context obsahuje viditelnou podkategorii Notebooky v Elektronice.
        """
        self.client.get(reverse('category_list'))
        subcategories = self.categories['electronics'].get_subcategories()
        self.assertIn(self.subcategories['laptops'], subcategories)

    def test_context_does_not_contain_hidden_subcategory(self) -> None:
        """
        Testuje, zda context neobsahuje skrytou podkategorii Tajná podkategorie v Elektronice.
        """
        self.client.get(reverse('category_list'))
        subcategories = self.categories['electronics'].get_subcategories()
        self.assertNotIn(self.subcategories['hidden_subcategory'], subcategories)

    def test_context_contains_visible_basic_phones(self) -> None:
        """
        Testuje, zda context obsahuje viditelnou pod-podkategorii Tlačítkové telefony v Mobily.
        """
        self.client.get(reverse('category_list'))
        sub_subcategories = self.subcategories['mobiles'].get_subcategories()
        self.assertIn(self.sub_subcategories['basic_phones'], sub_subcategories)

    def test_context_contains_visible_smartphones(self) -> None:
        """
        Testuje, zda context obsahuje viditelnou pod-podkategorii Chytré telefony v Mobily.
        """
        self.client.get(reverse('category_list'))
        sub_subcategories = self.subcategories['mobiles'].get_subcategories()
        self.assertIn(self.sub_subcategories['smartphones'], sub_subcategories)

    def test_context_does_not_contain_hidden_sub_subcategory(self) -> None:
        """
        Testuje, zda context neobsahuje skrytou pod-podkategorii Tajná pod-podkategorie v Mobily.
        """
        self.client.get(reverse('category_list'))
        sub_subcategories = self.subcategories['mobiles'].get_subcategories()
        self.assertNotIn(self.sub_subcategories['hidden_sub_subcategory'], sub_subcategories)
