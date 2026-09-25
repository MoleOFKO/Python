from itertools import combinations
import pandas as pd


def load_data(file_path):
    df = pd.read_csv(file_path)
    df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
    for col in ('Quantity','Unit_Price','Discount'):
        df[col] = pd.to_numeric(df[col], errors='coerce')
    df['Discount'] = df['Discount'].fillna(0).clip(0,1)
    df['Revenue'] = df['Quantity'] * df['Unit_Price'] * (1 - df['Discount'])
    return df


def association_rules(data, minimum_support=0.05, minimum_confidence=0.30):
    baskets = data.groupby('Customer_ID')['Product'].apply(lambda products: set(products)).tolist()
    basket_count = len(baskets)
    if not basket_count:
        return []
    def support(itemset):
        return sum(itemset.issubset(basket) for basket in baskets) / basket_count
    frequent = {}
    single_items = sorted({item for basket in baskets for item in basket})
    current = {frozenset([item]): support({item}) for item in single_items}
    current = {items: value for items, value in current.items() if value >= minimum_support}
    size = 1
    while current:
        frequent.update(current)
        size += 1
        previous = list(current)
        candidates = {
            frozenset(set(left) | set(right))
            for left, right in combinations(previous, 2)
            if len(set(left) | set(right)) == size
        }
        current = {
            itemset: support(itemset)
            for itemset in candidates
            if support(itemset) >= minimum_support
        }
    rules = []
    for itemset, itemset_support in frequent.items():
        if len(itemset) < 2:
            continue
        for item_count in range(1, len(itemset)):
            for left_tuple in combinations(sorted(itemset), item_count):
                left = frozenset(left_tuple)
                right = itemset - left
                left_support = frequent.get(left, support(left))
                right_support = frequent.get(right, support(right))
                confidence = itemset_support / left_support if left_support else 0
                lift = confidence / right_support if right_support else 0
                if confidence >= minimum_confidence:
                    rules.append({
                        'Rule': ', '.join(sorted(left)) + ' -> ' + ', '.join(sorted(right)),
                        'Support': round(itemset_support, 3),
                        'Confidence': round(confidence, 3),
                        'Lift': round(lift, 3),
                    })
    return sorted(rules, key=lambda r: r['Lift'], reverse=True)


df = load_data('d:/PROJECT/Python/Mini Project/e_commerce_example.csv')
rules = association_rules(df, 0.05, 0.30)
print('rows=', len(df))
print('customers=', df['Customer_ID'].nunique())
print('total_revenue=', round(float(df['Revenue'].sum()), 2))
print('items_sold=', int(df['Quantity'].sum()))
print('categories=', df.groupby('Category')['Order_ID'].nunique().to_dict())
print('category_revenue=', df.groupby('Category')['Revenue'].sum().round(2).to_dict())
print('rules_count=', len(rules))
for r in rules[:10]:
    print(r)
