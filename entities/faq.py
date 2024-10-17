# entities/faq_entity.py
from HU.Project.Website.dao.faq_dao import FAQDAO


class FAQ:
    @classmethod
    def get_faqs(self):
        """
        Fetches FAQ data from the database via the DAO.
        """
        return FAQDAO.fetch_faqs()  # Retrieves FAQ data from DAO
