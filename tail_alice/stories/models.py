from django.db import models

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail import blocks
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.images.blocks import ImageChooserBlock


class StoriesPage(Page):
    page_bg = models.ForeignKey(
        "wagtailimages.Image",
        help_text="Фон страницы",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    body = StreamField([
        ("title", blocks.CharBlock(required=True, verbose_name="Название книги?")),
        ("content", blocks.RichTextBlock(
            required=True,
            features=[
                "h1", "h2", "h3", "h4", "h5", "h6",
                "bold", "italic", "ol", "ul", "hr",
                "superscript", "subscript", "strikethrough",
                "image", "blockquote"],
            verbose_name="Содержимое главы")),
    ], block_counts={
        "title": {"max_num": 1},
    }, use_json_field=True, blank=True
    )

    class Meta:
        verbose_name = "Книга"

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [FieldPanel("page_bg"),
             FieldPanel("body")],
            heading="Книга",
            classname="collapsed",
        ),
    ]
