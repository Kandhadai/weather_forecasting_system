# dao/faq_dao.py
from HU.Project.Website.entities.db_connection import Database


class FAQDAO:
    @staticmethod
    def fetch_faqs():
        """
        Fetches FAQs from the database.
        """
        # Mockup for actual database query
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute('SELECT question, answer FROM faqs')
        faqs = cursor.fetchall()
        conn.close()
        return faqs
