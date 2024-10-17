# controls/faq_control.py
from HU.Project.Website.entities.faq import FAQ


class FAQControl:
    def get_faqs(self):
        """
        Executes the events in the use case: fetch all FAQs.
        """
        faqs = FAQ.get_faqs()  # The business logic resides in the entity
        return faqs

