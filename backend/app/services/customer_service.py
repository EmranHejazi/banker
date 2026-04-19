class CustomerService:

    @staticmethod
    async def search(search: Optional[str], filters: dict):
        return await CustomerRepository.search(search, filters)
