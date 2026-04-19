import csv
import io
import argparse
import asyncpg
from datetime import datetime
import jdatetime

CURRENT_YEAR = jdatetime.datetime.now().year

def normalize(value):
    if value is None:
        return None
    v = str(value).strip()
    return v if v != "" and v.lower() != "none" else None


def fix_birth_date(date_str: str):
    if not date_str:
        return None
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d").date()
        return dt.isoformat()
    except:
        pass
    try:
        y, m, d = map(int, date_str.split("-"))
        if d > 30:
            d = 30
        dt = datetime.strptime(f"{y}-{m:02d}-{d:02d}", "%Y-%m-%d").date()
        return dt.isoformat()
    except:
        return None


def extract_first_account(acc):
    if not acc:
        return None
    acc = acc.strip()
    if "|" in acc:
        return acc.split("|")[0].strip() or None
    return acc or None


async def import_file(pool, file_path: str, source_name: str):
    async with pool.acquire() as conn:
        print("Preparing CSV buffer for COPY...")

        buffer = io.StringIO()
        writer = csv.writer(buffer, delimiter="\t", lineterminator="\n")

        total = 0
        errors = 0

        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for raw_row in reader:
                row = {k.lower(): v for k, v in raw_row.items()}

                total += 1
                try:
                    national_code = normalize(row.get("national_code"))
                    account_number = extract_first_account(normalize(row.get("account_number")))
                    full_name = normalize(row.get("full_name"))
                    father_name = normalize(row.get("father_name"))
                    id_number = normalize(row.get("id_number"))

                    bd_raw = normalize(row.get("birth_date"))
                    birth_date = fix_birth_date(bd_raw)

                    age = None
                    if bd_raw and "-" in bd_raw:
                        try:
                            birth_year = int(bd_raw.split("-")[0])
                            age = CURRENT_YEAR - birth_year
                        except:
                            age = None

                    city_name = normalize(row.get("city_name"))
                    province_name = normalize(row.get("province_name"))
                    birth_city = normalize(row.get("birth_city"))
                    birth_province = normalize(row.get("birth_province"))
                    address = normalize(row.get("address"))
                    card_no = normalize(row.get("card_no"))
                    mobile = normalize(row.get("mobile"))
                    gender = normalize(row.get("gender"))

                    writer.writerow([
                        national_code,
                        account_number,
                        full_name,
                        father_name,
                        id_number,
                        birth_date,
                        age,
                        city_name,
                        province_name,
                        birth_city,
                        birth_province,
                        address,
                        card_no,
                        mobile,
                        gender,
                        source_name
                    ])
                except Exception:
                    errors += 1

        buffer.seek(0)

        # FIX: convert to bytes for asyncpg
        buffer_bytes = buffer.getvalue().encode("utf-8")
        byte_stream = io.BytesIO(buffer_bytes)

        print("COPY to customers…")
        async with conn.transaction():
            await conn.copy_to_table(
                table_name="customers",
                source=byte_stream,
                columns=[
                    "national_code",
                    "account_number",
                    "full_name",
                    "father_name",
                    "id_number",
                    "birth_date",
                    "age",
                    "city_name",
                    "province_name",
                    "birth_city",
                    "birth_province",
                    "address",
                    "card_no",
                    "mobile",
                    "gender",
                    "source"
                ],
                delimiter="\t",
                format="csv"
            )

        print(f"""
======== IMPORT DONE ========
File: {file_path}
Total rows: {total}
Inserted: {total - errors}
Errors: {errors}
=============================
""")


async def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--source", required=True)
    args = parser.parse_args()

    pool = await asyncpg.create_pool(
        user="banker",
        password="password",
        host="localhost",
        database="banker",
        port=5432,
        min_size=1,
        max_size=10
    )

    await import_file(pool, args.file, args.source)


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
