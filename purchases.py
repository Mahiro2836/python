import datetime

def filter_purchases_by_category(purchases, category):
    return [purchase for purchase in purchases if purchase[3] == category]

def filter_purchases_last_n_days(purchases, n):
    cutoff_date = datetime.date.today() - datetime.timedelta(days=n)
    return [
        purchase
        for purchase in purchases
        if datetime.datetime.strptime(purchase[4], "%Y-%m-%d").date() >= cutoff_date
    ]

def calculate_total_purchases_by_customer(purchases, callback):
    customer_totals = {}
    for purchase in purchases:
        customer_id = purchase[0]
        amount = callback(purchase[2])
        if customer_id in customer_totals:
            customer_totals[customer_id] += amount
        else:
            customer_totals[customer_id] = amount
    return customer_totals


def sort_purchases(purchases):
    return sorted(purchases, key=lambda x: (-x[2], x[3]))

def generate_customer_report(purchases, customer_id):
  customer_purchases = [
        {"product": purchase[1], "amount": purchase[2]}
        for purchase in purchases
        if purchase[0] == customer_id
    ]
  total_amount = sum(purchase["amount"] for purchase in customer_purchases)
  return {
        "customer_id": customer_id,
        "purchases": customer_purchases,
        "total_amount": total_amount
    }


if __name__ == "__main__":
    purchases = [
        [1, "Laptop", 1200, "Electronics", "2024-06-25"],
        [2, "Book", 30, "Books", "2024-06-28"],
        [1, "Mouse", 25, "Electronics", "2024-07-01"],
        [3, "T-shirt", 20, "Clothing", "2024-06-29"],
        [2, "Keyboard", 75, "Electronics", "2024-07-02"],
        [1, "Headphones", 100, "Electronics", "2024-07-03"],
        [4, "Jacket", 150, "Clothing", "2024-07-03"]
    ]


    filtered_electronics = filter_purchases_by_category(purchases, "Electronics")
    print("Покупки в категории 'Electronics':")
    for purchase in filtered_electronics:
      print(purchase)


    filtered_last_3_days = filter_purchases_last_n_days(purchases, 3)
    print("\nПокупки за последние 3 дня:")
    for purchase in filtered_last_3_days:
        print(purchase)


    customer_totals = calculate_total_purchases_by_customer(purchases, lambda x: x)
    print("\nСумма покупок каждого клиента:")
    for customer, total in customer_totals.items():
      print(f"Клиент {customer}: {total}")


    sorted_purchases = sort_purchases(purchases)
    print("\nОтсортированные покупки:")
    for purchase in sorted_purchases:
        print(purchase)
    
    customer_report = generate_customer_report(purchases, 1)
    print("\nОтчет для клиента 1:")
    print(customer_report)