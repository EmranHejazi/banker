class CustomerRepository:

    @staticmethod
    async def search(
        search: Optional[str],
        filters: dict,
        limit: int = 50,
        offset: int = 0
    ):
        query = """
        SELECT *
        FROM customers
        WHERE 1=1
        """

        params = {}

        # MAIN SEARCH — code / name / mobile
        if search:
            query += """
            AND (
                national_code ILIKE :search
                OR full_name ILIKE :search
                OR mobile ILIKE :search
            )
            """
            params["search"] = f"%{search}%"

        # FILTERS
        if filters.get("age"):
            query += " AND age = :age"
            params["age"] = filters["age"]

        if filters.get("city_name"):
            query += " AND city_name = :city_name"
            params["city_name"] = filters["city_name"]

        if filters.get("province_name"):
            query += " AND province_name = :province_name"
            params["province_name"] = filters["province_name"]

        if filters.get("birth_city"):
            query += " AND birth_city = :birth_city"
            params["birth_city"] = filters["birth_city"]

        if filters.get("birth_province"):
            query += " AND birth_province = :birth_province"
            params["birth_province"] = filters["birth_province"]

        if filters.get("gender"):
            query += " AND gender = :gender"
            params["gender"] = filters["gender"]

        query += " LIMIT :limit OFFSET :offset"
        params["limit"] = limit
        params["offset"] = offset

        async with db.pool.acquire() as conn:
            rows = await conn.fetch(query, *params.values())

        return [dict(row) for row in rows]
