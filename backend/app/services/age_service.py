from ..core.config import settings
from ..core.database import db

class AgeService:

    @staticmethod
    async def update_age_if_needed():
        query_check = """
        SELECT value::int FROM system_config WHERE key = 'current_year';
        """

        query_update_age = """
        UPDATE customers
        SET age = $1 - birth_year;
        """

        query_set_year = """
        UPDATE system_config SET value = $1 WHERE key = 'current_year';
        """

        async with db.pool.acquire() as conn:
            db_year = await conn.fetchval(query_check)

            if db_year != settings.CURRENT_YEAR:
                await conn.execute(query_update_age, settings.CURRENT_YEAR)
                await conn.execute(query_set_year, settings.CURRENT_YEAR)

        return {"status": "updated" if db_year != settings.CURRENT_YEAR else "no_change"}
