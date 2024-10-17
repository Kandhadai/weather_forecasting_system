# Remove this line:
# from HU.Project.Website.entities.data_export import DataExport

from HU.Project.Website.entities.db_connection import Database


class DataExportDAO:
    @staticmethod
    def _connect_to_db():
        return Database.connect()

    @classmethod
    def log_export(cls, data_export, export_path: str, export_format: str):
        """
        Logs the details of a data export to the database.
        """
        connection = cls._connect_to_db()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO data_exports (user_id, export_path, export_format) VALUES (%s, %s, %s)",
            (data_export.user_id, export_path, export_format)
        )
        connection.commit()
        cursor.close()
        connection.close()

    @classmethod
    def get_export_history(cls, user_id: int):
        """
        Retrieves the export history for a specific user.
        """
        connection = cls._connect_to_db()
        cursor = connection.cursor()
        cursor.execute("SELECT export_path, export_format FROM data_exports WHERE user_id = %s", (user_id,))
        history = cursor.fetchall()
        cursor.close()
        connection.close()
        return history
