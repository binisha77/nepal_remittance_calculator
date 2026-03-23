"""Nepal Remittance Calculator.

This script collects transactions, converts amounts to NPR,
tracks unique countries, and prints a formatted report.
"""

# Tuple-based exchange rates: (currency, NPR rate)
EXCHANGE_RATES = (
        ("USD", 132.0),
        ("AUD", 88.0),
        ("INR", 1.6),
        ("NPR", 1.0),
)


def get_rate(currency):
        """Return NPR conversion rate for a currency code."""
        currency = currency.upper()
        for code, rate in EXCHANGE_RATES:
                if code == currency:
                        return rate
        return None


def collect_transactions():
        """Collect transactions as a list of dictionaries."""
        transactions = []
        unique_countries = set()

        count = int(input("How many transactions do you want to enter? "))

        for i in range(count):
                print(f"\n--- Transaction {i + 1} ---")
                sender_name = input("Enter sender name: ").strip()
                receiver_name = input("Enter receiver name: ").strip()
                country = input("Enter sender country: ").strip()
                amount_sent = float(input("Enter amount sent: "))
                currency_type = input("Enter currency type (USD/AUD/INR/NPR): ").strip().upper()
                transaction_id = input("Enter transaction ID: ").strip()

                rate = get_rate(currency_type)
                if rate is None:
                        print("Unknown currency. Assuming NPR with rate 1.0")
                        rate = 1.0

                amount_npr = amount_sent * rate

                transaction = {
                        "sender_name": sender_name,
                        "receiver_name": receiver_name,
                        "country": country,
                        "amount_sent": amount_sent,
                        "currency_type": currency_type,
                        "transaction_id": transaction_id,
                        "rate": rate,
                        "amount_npr": amount_npr,
                }

                transactions.append(transaction)
                unique_countries.add(country)

        return transactions, unique_countries


def analyze_transactions(transactions):
        """Compute totals per country, highest transaction, and duplicate IDs."""
        totals_per_country = {}
        seen_ids = set()
        duplicate_ids = set()

        highest_transaction = None

        for tx in transactions:
                country = tx["country"]
                amount_npr = tx["amount_npr"]
                tx_id = tx["transaction_id"]

                totals_per_country[country] = totals_per_country.get(country, 0) + amount_npr

                if highest_transaction is None or amount_npr > highest_transaction["amount_npr"]:
                        highest_transaction = tx

                if tx_id in seen_ids:
                        duplicate_ids.add(tx_id)
                else:
                        seen_ids.add(tx_id)

        return totals_per_country, highest_transaction, duplicate_ids


def print_report(transactions, unique_countries, totals_per_country, highest_transaction, duplicate_ids):
        """Print a formatted remittance report."""
        print("\n" + "=" * 70)
        print("NEPAL REMITTANCE REPORT")
        print("=" * 70)

        print(f"\nTotal Transactions: {len(transactions)}")
        print(f"Unique Sender Countries: {len(unique_countries)} -> {sorted(unique_countries)}")

        print("\n--- Converted Transactions (to NPR) ---")
        for tx in transactions:
                print(
                        "ID: {id} | Sender: {sender} | Receiver: {receiver} | Country: {country} | "
                        "{amount:.2f} {currency} = {npr:.2f} NPR".format(
                                id=tx["transaction_id"],
                                sender=tx["sender_name"],
                                receiver=tx["receiver_name"],
                                country=tx["country"],
                                amount=tx["amount_sent"],
                                currency=tx["currency_type"],
                                npr=tx["amount_npr"],
                        )
                )

        print("\n--- Total Remittance Per Country (NPR) ---")
        for country, total in totals_per_country.items():
                print(f"{country}: {total:.2f} NPR")

        if highest_transaction:
                print("\n--- Highest Transaction ---")
                print(
                        f"Transaction ID: {highest_transaction['transaction_id']} | "
                        f"Amount in NPR: {highest_transaction['amount_npr']:.2f} | "
                        f"Country: {highest_transaction['country']}"
                )

        print("\n--- Duplicate Transaction IDs ---")
        if duplicate_ids:
                print(", ".join(sorted(duplicate_ids)))
        else:
                print("No duplicate transaction IDs found.")


def main():
        transactions, unique_countries = collect_transactions()
        totals_per_country, highest_transaction, duplicate_ids = analyze_transactions(transactions)
        print_report(
                transactions,
                unique_countries,
                totals_per_country,
                highest_transaction,
                duplicate_ids,
        )


if __name__ == "__main__":
        main()
