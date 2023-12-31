from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class HomePage(Page):
    page_bg = models.ForeignKey(
        "wagtailimages.Image",
        help_text="Фон страницы",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    navbar = StreamField([
        ("logo", ImageChooserBlock()),
        ("menu_item", blocks.PageChooserBlock())
    ], block_counts={
        "logo": {"max_num": 1},
    },use_json_field=True, max_num=6, blank=True
    )
    main = StreamField([
        ("heading", blocks.CharBlock(form_classname="title", verbose_name="Заголовок")),
        ("paragraph", blocks.RichTextBlock(verbose_name="Текст",
         features=["h2", "h3", "h4", "link", "document-link"])),
        ("image", ImageChooserBlock()),
    ], block_counts={
        "heading": {"min_num": 1, "max_num": 1},
    }, use_json_field=True, blank=True
    )
    footer = StreamField([
        ("contacts", blocks.RichTextBlock(verbose_name="Контакты",
         features=["h2", "h3", "h4", "image", "link", "document-link"])),
    ], use_json_field=True, max_num=1, blank=True
    )

    class Meta:
        verbose_name = "Главная"

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [FieldPanel("page_bg"),
             FieldPanel("navbar"),
             FieldPanel("main"),
             FieldPanel("footer")],
            heading="Главная страница",
            classname="collapsed",
        ),
    ]
