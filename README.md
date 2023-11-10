
```mermaid
flowchart TD
    Home-->page_bg--models.ForeignKey-->image;
    Home-->navbar-->StreamField--ImageChooserBlock-->logo-->{'max_num': 1};
    Home-->navbar-->StreamField--blocks.RichTextBlock-->menu_item-->{'min_num': 1};
    Home-->main-->StreamField--blocks.CharBlock-->heading-->{'min_num': 1};
    Home-->main-->StreamField--blocks.RichTextBlock-->paragraph;
    Home-->main-->StreamField--ImageChooserBlock-->image-->{'max_num': 5};
```