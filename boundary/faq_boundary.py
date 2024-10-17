# boundaries/faq_boundary.py
from HU.Project.Website.controls.faq_control import FAQControl


class FAQBoundary:
    def get_faqs(self):
        """
        This method takes no parameters and simply returns all FAQs.
        """
        control = FAQControl()
        return control.get_faqs()
